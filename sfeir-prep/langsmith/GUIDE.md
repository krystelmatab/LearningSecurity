# LangSmith — remise à niveau express (≈ 2 h)

Tu as dit maîtriser LangSmith : l'évaluateur peut tester ça en une question. L'objectif est de pouvoir **expliquer et montrer** les 4 usages ci-dessous sans hésiter.

## Les 4 choses à savoir expliquer

| Usage | Ce que c'est | Phrase à savoir dire |
|---|---|---|
| **Tracing** | Chaque appel de chaîne/agent devient une *trace* composée de *runs* (prompt, retriever, LLM, parser) avec entrées, sorties, latence, tokens, coût | « J'active `LANGSMITH_TRACING=true` et je vois exactement quel contexte le retriever a ramené et quel prompt final est parti au modèle. » |
| **Datasets** | Ensemble d'exemples (input + référence attendue), créés à la main, depuis un CSV ou depuis des traces de prod | « Je transforme les mauvaises réponses vues en prod en exemples de dataset : c'est ma non-régression. » |
| **Evaluators** | Fonctions qui notent une sortie : code (exact match, regex, JSON valide) ou **LLM-as-judge** (correctness, groundedness) | « Pour un RAG je mesure séparément : pertinence du retrieval, fidélité au contexte, justesse de la réponse. » |
| **Experiments** | Lancer une version de chaîne sur tout le dataset → scores comparables entre versions de prompt/modèle | « Avant de changer le prompt, je compare l'expérience A et B sur le même dataset. » |

Bonus à connaître de nom : **Prompt Hub / Playground** (versionner et tester des prompts dans l'UI), **annotation queues** (relecture humaine), **online evaluators** (évaluation automatique sur le trafic de prod), **monitoring** (dashboards latence/coût/erreurs), **metadata & tags** pour filtrer les traces (ex. par `user_id`).

## Pratique (à faire avant l'entretien)

1. Crée un compte gratuit sur smith.langchain.com → crée une clé API.
2. Configure :

```bash
export LANGSMITH_TRACING=true
```

```bash
export LANGSMITH_API_KEY=<ta clé>
```

```bash
export LANGSMITH_PROJECT=sfeir-prep
```

3. Lance `python ../corriges/chatbot_corrige.py` → ouvre le projet `sfeir-prep` dans l'UI. Clique sur une trace, déplie `RunnableLambda` : tu vois les chunks récupérés. **C'est la démo à savoir raconter.**
4. Lance `python demo_eval.py` → ouvre l'onglet *Datasets & Experiments* : tu vois le dataset et les scores.
5. Dans l'UI : ouvre une trace → *Add to dataset*. Puis *Playground* : modifie le prompt et relance.

## Questions qu'on pourrait te poser

- « Ton chatbot répond faux, comment tu investigues avec LangSmith ? » → trace → regarder le retriever d'abord (bon contexte ?) puis le prompt final, puis la sortie. Si le contexte est bon et la réponse fausse = problème de prompt/modèle ; si le contexte est mauvais = problème de retrieval.
- « Comment tu évites les régressions quand tu changes un prompt ? » → dataset de référence + experiment avant/après + seuil de score.
- « LLM-as-judge, c'est fiable ? » → utile à l'échelle, mais à calibrer contre un échantillon annoté par un humain ; juge avec un modèle différent/plus fort, critères précis, sortie binaire ou échelle courte.
- « Alternatives ? » → Langfuse (open source, self-hostable — argument souverainté chez les clients FR), Arize Phoenix, Vertex AI evaluation (contexte Google Cloud, pertinent chez SFEIR), MLflow.
