"""
"SFEIR HR Buddy" — chatbot RH interne (RAG + mémoire de conversation)
=====================================================================

Contexte client : une ESN veut un assistant qui répond aux questions des
collaborateurs sur la politique RH (télétravail, congés, formation).
Le POC a été écrit par un stagiaire. Il "marchait sur son poste",
mais en recette plus rien ne fonctionne. À toi de le débugger.

Lancer :  python chatbot_bugge.py
Par défaut MODE_DEMO = True -> un faux LLM est utilisé (pas besoin de clé).
"""

import os

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.documents import Document
from langchain_core.language_models import FakeListChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_text_splitters import RecursiveCharacterTextSplitter

MODE_DEMO = True

ANTHROPIC_API_KEY = "sk-ant-api03-Xk9fP2mQ7vR4tY8wZ1aB3cD5eF6gH0jK-prod"

# ---------------------------------------------------------------------------
# 1. Base de connaissances
# ---------------------------------------------------------------------------
POLITIQUE_RH = """
Télétravail : chaque collaborateur peut télétravailler jusqu'à 3 jours par semaine,
après validation de son manager. Le télétravail n'est pas possible pendant la période d'essai.

Congés : les collaborateurs disposent de 25 jours de congés payés et de 10 jours de RTT par an.
Les demandes de congés doivent être posées au moins 2 semaines à l'avance dans l'outil RH.

Formation : chaque collaborateur dispose d'un budget formation de 2000 euros par an.
Les certifications cloud (GCP, AWS, Azure) sont prises en charge à 100 %.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=400)
chunks = [Document(page_content=c) for c in splitter.split_text(POLITIQUE_RH)]


def retriever(question: str, k: int = 2) -> list[Document]:
    """Retriever naïf par mots-clés (remplace un vector store pour le POC)."""
    mots = set(question.lower().split())
    scored = []
    for doc in chunks:
        score = sum(1 for m in mots if m in doc.page_content.lower())
        scored.append((score, doc))
    scored.sort(key=lambda x: x[0])
    return [doc for _, doc in scored[:k]]


def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(d.page_content for d in docs)


# ---------------------------------------------------------------------------
# 2. LLM
# ---------------------------------------------------------------------------
if MODE_DEMO:
    llm = FakeListChatModel(
        responses=[
            "Vous pouvez télétravailler jusqu'à 3 jours par semaine.",
            "Vous m'avez demandé combien de jours de télétravail sont autorisés.",
            "Le budget formation est de 2000 euros par an.",
        ]
    )
else:
    from langchain_anthropic import ChatAnthropic

    llm = ChatAnthropic(
        model="claude-sonnet-latest",
        api_key=ANTHROPIC_API_KEY,
        temperature=1.0,
        max_tokens=30,
    )

# ---------------------------------------------------------------------------
# 3. Prompt
# ---------------------------------------------------------------------------
def build_prompt(user_question: str) -> ChatPromptTemplate:
    system = f"""Tu es HR Buddy, l'assistant RH de l'entreprise.
Voici la question du collaborateur : {user_question}
Réponds à partir du contexte suivant :
{{context}}"""
    return ChatPromptTemplate.from_messages(
        [
            ("system", system),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )


# ---------------------------------------------------------------------------
# 4. Chaîne RAG + mémoire
# ---------------------------------------------------------------------------
store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


def build_chain(user_question: str):
    prompt = build_prompt(user_question)
    rag_chain = (
        RunnablePassthrough.assign(
            context=RunnableLambda(lambda x: retriever(x["input"])) | format_docs
        )
        | prompt
        | llm
    )
    return RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )


def ask(question: str, user_id: str) -> str:
    chain = build_chain(question)
    answer = chain.invoke(
        {"input": question},
        config={"configurable": {"session_id": "default"}},
    )
    return answer.strip()


# ---------------------------------------------------------------------------
# 5. Démo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Alice >", "Combien de jours de télétravail puis-je faire ?")
    print("Bot   >", ask("Combien de jours de télétravail puis-je faire ?", user_id="alice"))

    print("Alice >", "Qu'est-ce que je viens de te demander ?")
    print("Bot   >", ask("Qu'est-ce que je viens de te demander ?", user_id="alice"))

    print("Bob   >", "Quel est mon budget formation ?")
    print("Bot   >", ask("Quel est mon budget formation ?", user_id="bob"))
