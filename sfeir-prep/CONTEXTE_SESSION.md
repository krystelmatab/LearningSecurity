# Contexte pour reprendre la préparation dans une nouvelle session

> À lire en premier par Claude au début de chaque nouvelle session.

## Qui je suis et ce que je prépare

- Je prépare un **entretien technique d'une heure en visio pour un poste de Consultante IA chez SFEIR**, orienté IA générative.
- Le poste mélange consultante IA (cadrage, conception de solutions, analyse de cas d'usage, dialogue avec les équipes techniques) et ingénieure IA (Python, LangChain, API, architecture, intégration).
- **Mon profil :** consultante IA / AVV IA dans mon poste actuel, **pas développeuse**. Je l'ai dit pendant les premiers échanges, en précisant que je sais prototyper des solutions IA.
- Pendant un premier échange, **j'ai dit maîtriser LangSmith** (observabilité, test de prompts). Ce n'est pas encore le cas : c'est un point à travailler en priorité.
- Je maîtrise les concepts généraux (LLM, RAG, MCP…) : **pas besoin de travailler la partie théorique.** Le focus est la pratique.

## Déroulé annoncé de l'entretien

1. **Intro (5-10 min)** : présentations, questions sur SFEIR.
2. **Questions techniques** : LLM, RAG, MCP, etc.
3. **Prompt engineering** : exercices de prompting et de structuration, probablement avec Claude ou LangChain.
4. **LangChain** : debugging d'un chatbot contenant plusieurs erreurs.

Comportement attendu : raisonner à voix haute, expliquer ses choix, collaborer avec l'évaluateur, poser des questions, demander de l'aide si bloquée, ne pas s'entêter. Une petite erreur de syntaxe n'est pas pénalisante si le raisonnement est bon.

## Le kit (dans ce dossier `sfeir-prep/`)

- `README.md` : ce que l'on sait des entretiens SFEIR (PlayOffs, pair programming, raisonnement valorisé), le planning sur 2 jours, les phrases clés, les questions à poser à l'évaluateur.
- `partie2-prompting/EXERCICES.md` : exercices P1 à P5 + `playground.py`.
- `partie3-langchain/` : `chatbot_bugge.py` (11 bugs) et `extracteur_bugge.py` (8 bugs), avec `ENONCE.md`.
- `langsmith/` : `GUIDE.md` + `demo_eval.py`.
- `corriges/` : **ne pas me montrer les corrigés avant que j'aie fait l'exercice.**
- `debriefs/` : un fichier de débrief par exercice terminé.

## Règles des simulations

- Claude joue **l'évaluateur SFEIR** (pas une personne réelle nommée) : il présente le contexte client, me relance, ne donne pas la solution, donne un indice seulement si je le demande, et répond à mes questions de cadrage en inventant des réponses client réalistes.
- Je tape **« Fin »** pour sortir du rôle : Claude écrit alors un débrief dans `sfeir-prep/debriefs/`, avec la note sur la grille (cadrage, structuration, vision prod, communication, collaboration, sur 5), mes points forts, les points à corriger, la solution idéale, et des exercices pour m'entraîner. Puis il commit et push.
- Je n'ai **rien installé en local**. Pour les exercices de code, Claude peut exécuter les fichiers dans son environnement et me montrer les sorties, ou me guider pour installer.
- Réponses en **français**, claires, structurées, sans remplissage.

## Avancement

| Étape | Statut |
|---|---|
| Simulation 1, exercice P1 (classifieur de mails) | ✅ Fait — débrief : `debriefs/simulation-1_P1_classifieur-mails.md` |
| Simulation 1, exercice P2 (critique d'un mauvais prompt) | ✅ Fait — débrief : `debriefs/simulation-1_P2_critique-prompt-CR.md` |
| Simulation 2 : debugging `chatbot_bugge.py` | ✅ Fait (15,5 / 25) — débrief : `debriefs/simulation-2_chatbot-bugge.md`. 4 plantages sur 4 corrigés (3 avec l'outil), 0 erreur silencieuse sur 8. Corrigé `corriges/partie3_bugs.md` lu pour le débrief. |
| Simulation 2 (à rejouer) : audit des erreurs silencieuses sans corriger | À faire — exercices 1 à 6 du débrief ; mon fichier `chatbot_bugge.py` contient mes corrections (non commité) |
| Simulation 2 bis : `partie3-langchain/exercice_cle_api/` (clé API fournie, vrai LLM) | **Prochaine étape** — énoncé créé, corrigé dans `corriges/exercice_cle_api.md` |
| LangSmith (guide + pratique) | À faire — prioritaire |
| Simulation 3 : P3 + P4 + `extracteur_bugge.py` | À faire |
| Simulation 4 : entretien blanc complet de 60 min, exercices inédits | À faire |

## Ce qu'on a appris sur moi (Simulation 1)

- **Point fort :** le cadrage. Je pose les bonnes questions (format de l'API, identifiants, règles de priorité métier, définitions des équipes).
- **À corriger :**
  - je ne teste pas moi-même les cas difficiles contre mon prompt avant de le livrer ;
  - j'oublie de définir les catégories et de délimiter les données (balises) ;
  - je ne précise pas la sortie attendue pour les cas limites (injection) ;
  - je n'intègre pas toujours ce que le client a validé pendant l'échange ;
  - j'ai confondu un test de fumée (5 exemples) avec un vrai jeu d'évaluation (échantillon de l'historique étiqueté) ;
  - utiliser un LLM pour concevoir un prompt (brain dump, puis « interviewe-moi ») est une pratique courante : la présenter comme une méthode maîtrisée, avec validation par moi sur les cas difficiles, jamais comme un renvoi de l'exercice.
- **Notions clarifiées après coup :** les balises XML servent de délimiteurs (pas du code), `{variable}` est remplacée par le code à chaque appel, `A | B` veut dire « une de ces valeurs ». Le prompt *guide*, le code *garantit*.

## Ce qu'on a appris sur moi (Simulation 1, P2)

- **Points forts :** cadrage (source, langue, données sensibles, périmètre), intégration des retours, honnêteté (« je ne sais pas, aide »), bon réflexe de contredire quand le contexte l'impose (chatbot : tout est rôle *user*, pas de variable remplacée par le code).
- **À corriger :**
  - faire le **diagnostic mot par mot** du prompt d'origine (« bien », « important », « créatif »… et la contradiction « ne pas inventer » / « sois créatif ») avant de réécrire ;
  - **mettre un exemple** dans le prompt, même court, sur le cas piège (action ambiguë, date absente) ;
  - traiter l'**attribution ambiguë**, pas seulement l'absence d'information ;
  - ne pas compter sur une **auto-relecture V1→V2 invisible** : citations/horodatages, ou deux appels tracés dans LangSmith ;
  - évaluation : référence validée par le client, comparaison ancien/nouveau prompt sur les mêmes cas, métriques précises, jeu de 20-30 cas ;
  - 80 pages : le contexte suffit peut-être, mais la qualité baisse → découpage + extraction puis rédaction (pas un RAG) ;
  - relire le prompt (fautes de frappe) ; réponses plus courtes (10 min visées, 30 réalisées).
- **Notion clarifiée :** en chatbot, la règle « refuse tout sauf le CR » doit autoriser les corrections du CR.

## Ce qu'on a appris sur moi (Simulation 2)

- **Points forts :** lecture avant exécution avec prédiction juste (overlap > chunk), repérage du modèle et de ses réglages, du prompt trop pauvre et du retriever par mots-clés ; relecture de chaque changement de l'assistant dans l'éditeur ; honnêteté (« je ne comprends pas ») ; vision client (jeu de test, évaluation avant prod).
- **À corriger :**
  - je travaille avec un assistant de code et je n'explique pas les erreurs avec mes mots : **expliquer chaque erreur en une phrase** ;
  - je rate les **erreurs silencieuses** (clé en dur, tri inversé, question dans le prompt système, mémoire effacée, **sessions partagées = fuite de données**) : classer en 3 familles *plante / faux sans planter / risque de prod* ;
  - je n'ai pas **vérifié l'unité** de `chunk_size` (caractères, pas tokens) : 20 / 10 est trop petit ; en POC, ne pas découper ou ~200 / 20-30 ;
  - je ne demande pas d'**indice** ; je répète ma méthode au lieu de répondre à la question posée ;
  - **LangSmith jamais cité** alors que je l'ai annoncé maîtrisé ;
  - respecter le chrono (25 min dépassées).
- **À poser en début d'entretien :** « Puis-je m'appuyer sur un assistant de code ? »
- **Mon fichier `chatbot_bugge.py`** contient mes corrections (non commité) : le copier avant de remettre l'original pour rejouer l'audit.
