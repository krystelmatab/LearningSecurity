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
| Simulation 2 : debugging `chatbot_bugge.py` | ⏭ **Prochaine étape** |
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
  - ne pas dire en entretien que j'utilise un chatbot pour concevoir mes prompts.
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
