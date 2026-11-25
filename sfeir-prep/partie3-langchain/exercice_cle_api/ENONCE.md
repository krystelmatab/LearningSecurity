# Exercice « clé API fournie par l'évaluateur » : configurer, lancer, débugger un programme qui appelle un vrai LLM

**Durée en conditions réelles : 25-30 min.** C'est la Simulation 2 bis : à faire avant ou après `chatbot_bugge.py`.

## Le scénario (tel que l'évaluateur le présentera)

> « On a un POC qui génère des comptes-rendus de réunion avec Claude. Je te donne une clé API temporaire, valable le temps de l'entretien. Configure ton environnement, lance le programme, et débugge-le. Parle à voix haute. »

Tu reçois la clé dans un message (chat de la visio). **Elle ne va dans aucun fichier du dépôt, et jamais dans un chat avec Claude.**

## Ce que cet exercice entraîne

1. **Installer** et lancer un projet que tu viens de cloner (terminal, `venv`, `pip`).
2. **Configurer une clé API** correctement (variable d'environnement ou `.env`).
3. **Lire les vraies erreurs** : module manquant, variable absente, erreur 401, erreur 404, erreur silencieuse.
4. **Repérer les bugs qui ne plantent pas** : sortie coupée, mauvais type de sortie, paramètres inadaptés, fuite de secret.
5. **Parler de production** : sécurité de la clé, gestion d'erreurs, évaluation.

## Préparation (5 min)

Depuis le dossier du dépôt cloné, avec ton `venv` actif et `pip install -r requirements.txt` déjà fait :

```bash
cd sfeir-prep/partie3-langchain/exercice_cle_api
```

Le dossier contient :
- `cr_reunion_bugge.py` : le programme à débugger ;
- `transcription_exemple.txt` : une réunion de test (avec des pièges) ;
- `.env.example` : un modèle de fichier `.env`.

## Les trois situations d'entraînement

Choisis celle qui correspond à ce que tu as sous la main. L'idéal est de les enchaîner.

| Situation | Ce que tu configures | Ce que tu peux valider |
|---|---|---|
| **A. Aucune clé** | rien | les erreurs de démarrage (module, variable absente) |
| **B. Fausse clé** `sk-ant-fake` | une variable d'environnement | tout jusqu'à l'**erreur 401**, comme si l'évaluateur t'avait donné une clé expirée |
| **C. Vraie clé** (la tienne, console.anthropic.com, ou celle de l'évaluateur) | une variable d'environnement | tout le programme, y compris la qualité de la sortie |

Si tu n'as pas de vraie clé, `USE_FAKE_LLM=1` remplace le modèle par un faux : ça te permet de tester la logique du programme (ce n'est pas un bug, c'est un outil d'entraînement).

## Comment définir la clé dans le terminal

Mac / Linux :

```bash
export ANTHROPIC_API_KEY="la-clé"
```

Windows (PowerShell) :

```bash
$env:ANTHROPIC_API_KEY="la-clé"
```

Pour vérifier que Python **voit** la clé, sans l'afficher :

```bash
python -c "import os; print('clé présente :', 'ANTHROPIC_API_KEY' in os.environ)"
```

(`python3` sur Mac/Linux si besoin.) Ces variables n'existent que dans le terminal où tu les as tapées : si tu ouvres un autre terminal, tu les refais.

L'autre option est un fichier `.env` : copie `.env.example` en `.env`, remplace la valeur, et le code le charge avec `python-dotenv`. **Le `.env` ne doit jamais être commité** : vérifie qu'il est dans `.gitignore`.

## Ta mission

1. **Lire le code avant de l'exécuter** (3 min) et dire à voix haute ce qui te choque.
2. **Lancer** : `python cr_reunion_bugge.py transcription_exemple.txt`. Lire l'erreur, formuler une hypothèse, corriger, relancer.
3. Quand quelque chose s'affiche, **ne t'arrête pas** : vérifie que le CR est correct (complet ? fidèle ? bon format ?).
4. En fin d'exercice, résume en 1 minute les problèmes **par catégorie**, et ce que tu ferais avant la mise en production.

## Règles de sécurité (à appliquer aussi pendant l'entretien)

- Ne colle jamais la clé dans le chat de l'évaluateur, dans un fichier du dépôt, ni dans un message à Claude.
- Si une clé apparaît dans un log ou dans un commit, on considère qu'elle est **compromise** : on la révoque.
- Si tu bloques sur l'environnement, dis-le tôt : « Je suis bloquée sur l'installation, tu peux me débloquer ? »

## Indices de catégories (lis seulement si bloquée plus de 5 min)

<details><summary>Afficher les catégories</summary>

- Environnement / dépendances (×1)
- Configuration de la clé API (×1)
- Sécurité (×1)
- Cohérence prompt ↔ chaîne (×1)
- Paramètres du modèle (×3)
- Gestion des erreurs (×1)
- Type de sortie (×1)
- Qualité du prompt (×1)

</details>

## Phrases utiles pendant l'exercice

- « L'erreur dit `ModuleNotFoundError: dotenv` : la bibliothèque n'est pas installée dans mon `venv`. Je l'installe, et je regarde si elle devrait être dans le `requirements.txt`. »
- « `KeyError` sur le nom de la variable : le code lit un nom, mais la clé est dans un autre. Je compare les deux. »
- « Une erreur 401, c'est le serveur qui refuse la clé. Le problème n'est pas dans le code mais dans l'authentification. Une 404, c'est plutôt un nom de modèle qui n'existe pas. »
- « Ça ne plante plus, mais la sortie est vide : je soupçonne une erreur avalée quelque part. »
- « Avant la prod, j'ajouterais : une clé gérée par un gestionnaire de secrets, des logs sans secrets, des tests sur des cas pièges, et des traces LangSmith. »

## Pour t'entraîner ensuite

1. Refais l'exercice une seconde fois, chrono en main, sans regarder l'énoncé.
2. Écris le prompt d'origine sous une forme corrigée (P2) et vérifie sur `transcription_exemple.txt` que l'action ambiguë de Marie/Paul est traitée comme prévu.
3. Active LangSmith (`langsmith/GUIDE.md`) sur ce programme et regarde la trace d'un appel.
