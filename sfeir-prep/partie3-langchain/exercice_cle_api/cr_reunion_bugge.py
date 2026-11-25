"""
"CR Buddy" — générateur de comptes-rendus de réunion (POC)
==========================================================

Contexte client : un assureur veut transformer ses transcriptions de réunion
en comptes-rendus d'une page (décisions, actions, points ouverts).
Le POC a été écrit à la va-vite par un collègue, avec la clé API de l'équipe.
Il "marchait sur son poste". Sur le tien, rien ne se passe comme prévu.

Lancer :  python cr_reunion_bugge.py transcription_exemple.txt

Ce programme appelle un vrai modèle : il faut une clé API (ANTHROPIC_API_KEY).
Entraînement sans clé : USE_FAKE_LLM=1 remplace le modèle par un faux
(ce n'est PAS un bug : c'est un outil de test).
"""

import os
import sys

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.language_models import FakeListChatModel
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

API_KEY = os.environ["ANTHROPIC_KEY"]
print(f"[debug] clé chargée : {API_KEY}")

if os.environ.get("USE_FAKE_LLM") == "1":
    llm = FakeListChatModel(
        responses=["Résumé : le comité a validé la campagne de tests. Décision : campagne avant fin du mois."]
    )
else:
    llm = ChatAnthropic(
        model="claude-sonet-5",
        api_key=API_KEY,
        temperature=1.0,
        max_tokens=60,
    )

SYSTEM = """Tu es un assistant qui rédige des comptes-rendus de réunion.
Sois créatif. Fais attention à ne pas inventer.
Voici la transcription : {transcript}"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM),
        ("human", "Rédige le compte-rendu."),
    ]
)

chain = prompt | llm


def generer_cr(transcription: str) -> str:
    try:
        resultat = chain.invoke({"transcription": transcription})
    except Exception:
        return ""
    return resultat


if __name__ == "__main__":
    chemin = sys.argv[1] if len(sys.argv) > 1 else "transcription_exemple.txt"
    with open(chemin, encoding="utf-8") as f:
        texte = f.read()

    cr = generer_cr(texte)
    print("\n=== COMPTE-RENDU ===")
    print(cr)
