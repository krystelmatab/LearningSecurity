# Corrigé Partie 3 — les 11 bugs du chatbot RH

> ⚠️ Ne pas lire avant d'avoir fait l'exercice en simulation.

## Ordre dans lequel ils apparaissent

### Bugs qui font planter (trouvés en lançant)

| # | Ligne / zone | Symptôme | Correction | Ce qu'il faut dire |
|---|---|---|---|---|
| 2 | `chunk_overlap=400` | `ValueError: larger chunk overlap than chunk size` | `chunk_overlap=30` (10-20 % du chunk_size) | « L'overlap sert à ne pas couper une idée entre deux chunks ; il doit être plus petit que le chunk. » |
| 6a | `("human", "{question}")` | `KeyError … missing variables {'history','question'}` | `{input}` | « La chaîne envoie `input`, le prompt attend `question` : contrat d'interface cassé. » |
| 6b | `MessagesPlaceholder("history")` vs `history_messages_key="chat_history"` | même KeyError | aligner les deux noms | « RunnableWithMessageHistory injecte l'historique sous la clé `history_messages_key`, le placeholder doit porter le même nom. » |
| 9 | `answer.strip()` | `AttributeError: 'AIMessage' has no attribute 'strip'` | ajouter `\| StrOutputParser()` (ou `.content`) | « Un chat model renvoie un AIMessage, pas une str. » |

### Bugs silencieux (le programme tourne, mais c'est faux) — **ce sont eux qui font la différence**

| # | Zone | Problème | Correction | Risque métier |
|---|---|---|---|---|
| 8 | `get_session_history` | recrée un historique vide à chaque appel → aucune mémoire | `if session_id not in store:` | Le bot ne se souvient pas de la question précédente |
| 11 | `session_id: "default"` (+ `user_id` jamais utilisé) | tous les utilisateurs partagent la même conversation | `session_id: user_id` | **Fuite de données** entre collaborateurs (RGPD) |
| 3 | `scored.sort(key=...)` | tri croissant → renvoie les chunks **les moins** pertinents | `reverse=True` | Hallucinations : le LLM n'a pas le bon contexte |
| 5 | `build_prompt(user_question)` en f-string | la question utilisateur est injectée dans le **system prompt** | template fixe, question dans le message `human` | **Prompt injection** + crash si la question contient `{` `}` |
| 1 | `ANTHROPIC_API_KEY = "sk-ant-..."` | secret en dur dans le code | variable d'env / Secret Manager, rotation de la clé | Clé de prod commitée dans Git |
| 4 | `ChatAnthropic(...)` | modèle `claude-sonnet-latest` inexistant, `temperature=1.0`, `max_tokens=30` | nom de modèle figé, `temperature=0`, `max_tokens` ~1024 | Erreur 404 en mode réel ; réponses créatives et tronquées pour un cas factuel |
| 10 | `build_chain()` appelé à chaque `ask()` | chaîne reconstruite à chaque question | construire une fois au démarrage | Perf + c'est ce qui rendait le bug 5 possible |
| 7 | system prompt | pas de consigne de grounding | « réponds uniquement depuis le contexte, sinon dis que tu ne sais pas » | Hallucinations sur des sujets RH sensibles |

## Points bonus à mentionner à la fin (niveau consultant)

- **`InMemoryChatMessageHistory` est déprécié** (warning affiché) : en prod, mémoire persistante (Redis, Firestore, Postgres) et, pour du neuf, LangGraph + checkpointer.
- **Observabilité** : activer LangSmith (`LANGSMITH_TRACING=true`) pour voir le contexte réellement récupéré → c'est comme ça qu'on aurait vu le bug 3 en 10 secondes.
- **Évaluation** : créer un dataset de 20 questions RH avec réponses attendues et lancer un évaluateur (correctness + groundedness) avant chaque changement de prompt.
- **Retriever** : remplacer le keyword matching par un vector store (embeddings) ou un hybride BM25 + vecteurs.
- **Tests** : un test unitaire qui vérifie que deux `user_id` différents ont deux historiques séparés.

## Grille d'évaluation probable

| Critère | Ce qui est attendu |
|---|---|
| Méthode | Lire avant d'exécuter, lire la stacktrace en entier, corriger un bug à la fois |
| Communication | Hypothèse → vérification → conclusion, à voix haute |
| Profondeur | Ne pas s'arrêter quand « ça tourne » |
| Vision prod | Sécurité, données personnelles, observabilité, coût |
| Collaboration | Demander, accepter un indice, ne pas s'entêter |

Un bon score ≈ 4 crashs + au moins 4 bugs silencieux dont **sessions partagées** et **prompt injection**.
