# Débrief — Simulation 2 bis : `cr_reunion_bugge.py` (clé API fournie, vrai LLM)

*Durée : ~25 min d'échange, chrono abandonné à ta demande. **Exercice arrêté avant la première exécution** : tu as corrigé ensuite avec un autre assistant de code, hors de la simulation.*
*Ce débrief juge ce que tu as montré **pendant l'échange**. Les corrections visibles dans ton fichier sont comptées à part.*

## En bref

**Ton point fort : le cadrage et le diagnostic du prompt, à voix haute.** Avant de toucher à quoi que ce soit, tu as demandé : quelles réunions, quelle taille maximale, faut-il un pipeline de découpage pour 80 pages, quel format le client attend-il ? Tu as aussi diagnostiqué le prompt (« créatif » contredit « pas d'invention », format absent, longueur absente, cas limites absents) et la température.

**Ce qui a manqué :**
- la **clé affichée à l'écran** : repérée seulement après ma relance. C'était pourtant le risque n°1 de la fiche ;
- **7 des 9 bugs** jamais évoqués pendant l'échange (voir tableau) ;
- aucun **plantage lu ni expliqué** : tu n'as rien lancé ;
- l'**arrêt de l'exercice** au moment où il devenait utile.

**Verdict probable d'un évaluateur SFEIR :** « Très bon cadrage, bon regard sur le prompt. Mais n'a pas lancé le programme, a laissé passer la clé en clair, et s'est reposée sur un outil sans pouvoir expliquer. » Niveau **moyen**.

## Le point à regarder en face

Tu m'as dit : « Avec l'assistant de code, j'ai très bien compris les erreurs, mais impossible de les expliquer à voix haute de cette manière. »

| Ce que tu dis | Ce qu'un évaluateur entend |
|---|---|
| « J'ai compris avec l'assistant » | Rien : il ne voit pas ce que tu as compris. |
| « J'explique ensuite » | Trop tard : l'entretien dure une heure, il juge **en direct**. |

**Ce qui compte n'est pas de ne pas utiliser l'assistant, mais de pouvoir dire en une phrase : « la clé était affichée, donc elle serait apparue dans la visio et les logs ».** Cette phrase s'entraîne. Voir l'exercice 1 ci-dessous.

Deux remarques justes de ta part, que je retiens :
- tu avais raison de relever que je t'avais promis une clé sans te la donner. En vrai entretien, l'évaluateur la colle dans le chat de la visio. Ici, le mode « faux modèle » était la bonne solution ;
- tu as eu le bon réflexe sur la clé : `.env` + bibliothèque dédiée, jamais dans le code.

## Ta note sur la grille

| Critère | Note | Commentaire |
|---|---|---|
| Cadrage / méthode | **3 / 5** | Excellent cadrage client (types de réunion, taille, pipeline long, format). Lecture avant exécution. Mais aucune exécution, donc aucune hypothèse testée, et tu as lu le code « en survol » (clé affichée, nom du modèle, `max_tokens` non repérés). |
| Structuration | **2,5 / 5** | Ta réflexion est riche mais parle de tout en même temps. Toujours pas de classement « plante / faux sans planter / risque de prod ». |
| Vision prod | **2 / 5** | Pas de mention de LangSmith, de jeu de test, de gestion des erreurs ni de revue sécurité. La clé affichée n'a été vue qu'avec une relance. Le résumé final et « avant la prod » n'ont pas eu lieu. |
| Communication | **2,5 / 5** | Raisonnement à voix haute agréable à suivre et honnête (« je ne suis pas développeuse », « il me faut la clé »). Mais ma question « pourquoi est-ce grave d'afficher cette clé, pour un directeur ? » est restée sans réponse. |
| Collaboration | **2,5 / 5** | Bonnes questions sur l'énoncé et sur le client, honnêteté sur tes limites. Mais tu n'as pas demandé d'indice, et tu as arrêté l'exercice plutôt que de signaler ce qui te bloquait pendant. |

**Total : 12,5 / 25** (contre 15,5 pour la Simulation 2). La baisse vient de l'arrêt avant exécution, pas d'un manque de raisonnement.

## Bugs trouvés et ratés (comparaison avec le corrigé)

Le corrigé liste 9 bugs, plus la qualité du prompt (10ᵉ point). Légende : ✅ dit pendant l'échange · 🟡 corrigé dans ton fichier avec l'assistant, jamais expliqué à l'oral · ❌ raté.

| # | Zone | Pendant l'échange | Dans ton fichier |
|---|---|---|---|
| 1 | `python-dotenv` absent de `requirements.txt` | ❌ (rien lancé) | 🟡 Ajouté. |
| 2 | Variable `ANTHROPIC_KEY` ≠ `ANTHROPIC_API_KEY` | ❌ Tu as dit « la clé n'est pas dans le code », sans voir le nom lu. | 🟡 Corrigé, et lu seulement en mode réel. |
| 3 | La clé est affichée (`print`) | 🟡 **Vu après ma relance.** | 🟡 Ligne supprimée. |
| 4 | `{transcript}` dans le prompt, `transcription` à l'appel | ❌ | 🟡 Aligné. |
| 5 | `except Exception: return ""` : erreur avalée | ❌ | 🟡 Supprimé, commentaire explicite. |
| 6 | Modèle `claude-sonet-5` (faute de frappe) | ❌ Tu as cherché une faute… sur « human » (qui était correct). | 🟡 Nom corrigé. |
| 7 | `max_tokens=60` : CR coupé | ❌ | 🟡 1500. |
| 8 | `temperature=1.0` | ✅ **Dit dès la lecture**, avec la bonne raison. | 🟡 0,2 (le corrigé propose 0 : à discuter). |
| 9 | Retour = objet message, pas texte | ❌ | 🟡 `.content`. |
| 10 | Qualité du prompt (« sois créatif », format, cas limites) | ✅ **Très bon diagnostic à voix haute.** | 🟡 Prompt réécrit : voir ci-dessous. |

**Bilan : 2 repérés seuls (température, qualité du prompt), 1 après relance (clé affichée), 7 ratés pendant l'échange. Dans ton fichier final, les 9 sont corrigés.**

### Ce que ton prompt réécrit fait bien

- une page maximum, en français, trois rubriques imposées ;
- « n'invente ni fait, ni nom, ni date, ni chiffre » ;
- responsable absent → « à définir » ;
- balises `<transcription>` et consigne contre l'injection de prompt (même si l'exercice ne te l'avait pas demandé) ;
- cas « rubrique vide » traité.

### Ce qu'il reste à regarder dans ton prompt

| Point | Pourquoi |
|---|---|
| « Reprends les noms et numéros de dossier tels qu'ils apparaissent » | Le client a parlé de numéros de dossiers d'assurés. Ils sont repris dans un CR envoyé à la direction : **à valider avec le client** (données personnelles). Le corrigé demande de ne pas citer les noms de clients. |
| « Pour quand » sans règle « non précisée » | Si la date n'est pas dite, le modèle peut en inventer une. |
| Cas Marie/Paul de la transcription (« Ça dépend de toi, Paul, non ? ») | « Responsable clair » est vague : une attribution **non acceptée** doit devenir un point ouvert, pas une action. |
| `temperature=0,2` | `0` est plus prévisible pour un CR. |
| Pas de `timeout` ni de nouvel essai | En prod, un appel qui reste bloqué fige le service. |

## Bonnes habitudes à reproduire

- **Cadrer avant de coder** : tu as posé les bonnes questions, y compris le cas des documents très longs.
- **Diagnostic du prompt mot par mot** : « créatif » contre « ne pas inventer ».
- **Savoir où la clé doit aller** : `.env` + chargement, pas dans le code.
- **Dire quand tu ne peux pas faire** quelque chose (clé, voix) plutôt que de faire semblant.
- **Mettre en place le mode « faux modèle »** pour tester sans clé.

## À corriger

1. **Lancer avant de conclure.** Même avec un faux modèle : la première erreur te guide.
2. **Lire le code en 3 passes** : (a) secrets et noms, (b) réglages du modèle, (c) ce qui arrive en cas d'erreur.
3. **Répondre à la question posée**, même en une phrase, avant d'ajouter du contexte.
4. **Demander un indice** plutôt que d'arrêter.
5. **Expliquer chaque correction de l'assistant en une phrase**, surtout celles que tu n'as pas trouvées seule.
6. **Ne pas arrêter un exercice qui devient inconfortable** : en entretien, on ne peut pas.
7. **Ranger tes fichiers de travail** : voir « À savoir » ci-dessous.

## Exercices pour t'entraîner

1. **Explique ton propre diff (15 min, à l'écrit).** Lance `git diff -- sfeir-prep/partie3-langchain/exercice_cle_api/cr_reunion_bugge.py`. Pour chaque ligne changée, écris en une phrase : *ce qui était faux / l'effet / le risque pour le client*. Tu as déjà les corrections : il te manque les explications. Ensuite compare avec le tableau ci-dessus.
2. **Lecture en 3 passes (5 min).** Sur le fichier d'origine (`git show HEAD:sfeir-prep/partie3-langchain/exercice_cle_api/cr_reunion_bugge.py`), liste uniquement : secrets, noms, réglages. Sans corriger.
3. **Lire les codes d'erreur.** À savoir en 10 secondes : 401 = la clé est refusée, 404 = le nom du modèle n'existe pas, 429 = trop de requêtes, 5xx = problème chez le fournisseur.
4. **Réponse à la question « pourquoi afficher la clé est grave ? »** (30 secondes à voix haute) : « Elle serait visible dans le partage d'écran, dans les logs et dans l'historique de Git. Quelqu'un pourrait l'utiliser aux frais du client. On la révoque aussitôt. »
5. **Prompt, 2ᵉ version.** Ajoute dans ton prompt la règle « date non précisée » et le cas « attribution contestée ». Teste sur le passage Marie/Paul de `transcription_exemple.txt`.
6. **LangSmith.** Active le suivi sur ce programme et regarde la trace d'un appel : tu verras le prompt réellement envoyé et la réponse brute (`langsmith/GUIDE.md`).

## À savoir : état de tes fichiers (non commités)

| Fichier | Statut | Que faire |
|---|---|---|
| `exercice_cle_api/.env.example` | **Supprimé** | Le restaurer : c'est le modèle de configuration de l'exercice. |
| `exercice_cle_api/.env copy.example` | Nouveau | Probablement une copie par erreur : à supprimer ou renommer. |
| `exercice_cle_api/cr_reunion_gemini.py` | Nouveau | Variante Gemini : à garder hors du dépôt, sauf si tu veux la commiter. |
| `.env` | Ignoré par Git | Bien : c'est le but. Vérifie qu'il ne contient pas de clé réelle si tu partages ton écran. |

## Phrases utiles

- « Avant de lancer : je lis d'abord les secrets, les noms, puis les réglages du modèle. »
- « Le programme affiche la clé : c'est un secret, il finit dans les logs. Je le supprime et, si elle a été vue, je la révoque. »
- « Ça ne plante plus, mais le CR est-il complet, fidèle, sans invention ? »
- « 401, c'est la clé. 404, c'est le modèle. Ce n'est pas le même problème. »
- « Avant la prod : clé dans un gestionnaire de secrets, logs sans secrets, jeu de tests avec cas pièges, traces LangSmith. »
