# Partie 3 — Debugging d'un chatbot LangChain

**Durée en conditions réelles : 20-25 min.** Chrono lancé dès que tu ouvres le fichier.

## Le contexte (tel que l'évaluateur te le présentera)

> « Un client nous a livré ce POC de chatbot RH : RAG sur la politique interne + mémoire de conversation. Ça ne marche pas en recette. Prends le temps de lire le code, dis-moi à voix haute ce que tu vois, et on corrige ensemble. Il y a plusieurs erreurs, de natures différentes. »

## Installation

```bash
pip install -r requirements.txt
```

```bash
python chatbot_bugge.py
```

`MODE_DEMO = True` → un faux LLM répond (aucune clé nécessaire). Les bugs restent visibles.

## Ta mission

1. **Lire le code AVANT de l'exécuter** (2-3 min) et commenter à voix haute ce qui te choque.
2. Lancer, lire la stacktrace, corriger. Recommencer.
3. Quand ça tourne : **ne t'arrête pas.** Les bugs les plus importants ne font pas planter le programme.
4. À la fin : résume en 1 minute les problèmes par catégorie et ce que tu ferais avant la mise en prod.

## Indices de catégories (lis seulement si bloquée > 5 min)

<details><summary>Afficher les catégories</summary>

- Sécurité (×2)
- Configuration du RAG (×2)
- Cohérence prompt ↔ chaîne (×2)
- Mémoire / sessions (×2)
- Paramètres du LLM (×1)
- Type de sortie (×1)
- Architecture / performance (×1)

</details>

## Phrases utiles pendant l'exercice

- « Avant de lancer, je lis le flux de données de haut en bas : documents → chunks → retriever → prompt → LLM → sortie. »
- « L'erreur dit `missing variables {'history', 'question'}` : le prompt attend des noms que la chaîne ne fournit pas. Je vérifie les clés une par une. »
- « Ça tourne, mais je veux vérifier le *comportement* : est-ce que la mémoire est vraiment conservée ? Je vais afficher la taille de l'historique. »
- « Là je ne suis pas sûre de la signature de `RunnableWithMessageHistory`, je peux vérifier la doc ou tu préfères que je fasse une hypothèse ? »
