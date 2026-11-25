# Débrief — Simulation 2 : debugging de `chatbot_bugge.py` (chatbot RH, LangChain)

*Durée réelle : plus de 35 min (prévu : 25 min). Le chrono a été dépassé ; en entretien, il est strict.*
*Cadre : tu as travaillé avec un assistant de code (« vibe coding »), pas seule. Ce débrief juge ce que tu as montré, dans ce cadre.*

## En bref

**Ton point fort : la lecture « consultante » du code, avant de lancer.** Sans exécuter, tu as repéré : le chunk plus petit que l'overlap (et prédit que ça planterait : c'était juste), le modèle et ses réglages (température, longueur max), le prompt trop pauvre (pas de format, pas de cas « hors base », risque de « oublie tes consignes »), et le retriever par mots-clés. Tu as aussi pensé à la suite : jeu de test fourni par le client, évaluation avant la prod.

**Ce qui a manqué :**
- les **erreurs silencieuses** (le programme tourne mais c'est faux) : 2 repérées à la lecture sur 8 (modèle et réglages, consigne de réponse), aucune corrigée. Les plus parlantes pour un client (clé secrète, conversations partagées) sont passées à côté ; elles ne demandent pas de savoir programmer ;
- les **explications avec tes mots** : tu as corrigé 3 erreurs de « plantage » avec l'outil, mais je n'ai pas entendu pourquoi elles plantaient ;
- la **vérification de ce que l'outil propose**.

**Verdict probable d'un évaluateur SFEIR :** « Bonne lecture de départ et bonne vision du cadre client, mais s'appuie beaucoup sur l'outil et a laissé passer les risques les plus visibles pour le client (clé secrète, conversations partagées). » Niveau **moyen**. C'est le point le plus entraînable de toute ta préparation.

## Ce que cet exercice mesure vraiment (réponse à ta question)

Tu as dit que tu te sentais jugée comme une développeuse. Voici ce qui est attendu, et ce qui ne l'est pas.

| Pas attendu | Attendu |
|---|---|
| Taper vite ou connaître les noms exacts des fonctions | Lire, faire une hypothèse, la tester, expliquer |
| Trouver seule toutes les erreurs de nommage | Dire pourquoi un plantage a eu lieu, avec tes mots |
| Se passer d'assistant (à confirmer avec l'évaluateur) | Contrôler ce que l'assistant propose |

**Ta vraie valeur de consultante est dans les erreurs silencieuses.** Une erreur qui plante, l'assistant la voit tout seul. Une erreur qui laisse le programme tourner (tous les collaborateurs dans la même conversation, le mauvais contexte envoyé au modèle, une clé secrète dans le code), il ne la signale pas forcément. Là, ton jugement fait la différence. Les 6 bugs que tu as ratés sont tous de ce type. Parmi eux, **la clé secrète et les conversations partagées se repèrent par bon sens**, sans savoir programmer : ce sont les 2 à viser en priorité. Les trois autres (tri, mémoire effacée, chaîne reconstruite) relèvent plutôt du métier d'ingénieure.

## Ta note sur la grille

| Critère | Note | Commentaire |
|---|---|---|
| Cadrage / méthode | **3 / 5** | Lecture avant exécution, prédiction (« ça va planter »), une erreur à la fois, relecture des changements dans l'éditeur : bonne méthode. Mais tu t'es vite reposée sur l'outil sans le questionner, et tu n'as pas cadré le client (qui utilise le chatbot ? combien d'utilisateurs ?). |
| Structuration | **3 / 5** | Ta liste à la lecture est riche, mais en vrac, sans hiérarchie. Il manque : « ce qui plante / ce qui est faux sans planter / ce qui est un risque ». |
| Vision prod | **3 / 5** | Bien : jeu de test du client, évaluation avant la prod, hors-sujet, vector store. Manquent : la sécurité (clé, conversations partagées), l'observabilité (LangSmith jamais cité) et la réponse à « comment tu t'en rends compte en prod ? ». |
| Communication | **3 / 5** | Honnête (« je ne comprends pas », « j'aurais pas vu »), bonne prédiction. Mais plusieurs de mes questions sont restées sans réponse directe (les tokens, le `KeyError`, la fiabilité de la liste de l'outil), et les hypothèses restent floues (« les bonnes variables »). |
| Collaboration | **3,5 / 5** | Tu as dit franchement où tu en étais, tu as posé une question de fond sur l'exercice, tu as accepté les relances. À améliorer : tu n'as jamais demandé d'indice, alors qu'il est prévu et bien vu. |

**Total : 15,5 / 25.**

## Bugs trouvés et ratés (comparaison avec le corrigé)

Le corrigé liste 11 bugs. Le score visé est « 4 plantages + au moins 4 erreurs silencieuses ».

| # | Zone | Statut | Remarque |
|---|---|---|---|
| 2 | Overlap plus grand que le chunk | ✅ Trouvé à la lecture | Prédit avant de lancer. **Mais la correction (20 / 10) est à revoir** : voir plus bas. |
| 6a, 6b | Noms `question` / `history` ≠ `input` / `chat_history` | 🟡 Corrigé avec l'outil | Correction juste dans ton fichier. Tu n'as pas expliqué la cause avec tes mots. |
| 9 | Réponse du modèle = objet, pas texte (`.strip()`) | 🟡 Corrigé avec l'outil | `answer.content.strip()` est une correction valable. |
| 4 | Nom du modèle, température 1, 30 tokens max | ✅ Repéré à la lecture | Les 3 points. Bon réflexe : vérifier le nom dans la documentation. |
| 7 | Pas de consigne « réponds seulement depuis le contexte » | ✅ Repéré à la lecture | Tu as demandé « que se passe-t-il si la question n'est pas dans la base ? ». |
| 1 | Clé secrète écrite dans le code | ❌ Raté | Aucune mention. Un évaluateur s'attend à ce que tu le voies. |
| 3 | Tri à l'envers : on renvoie les passages **les moins** pertinents | ❌ Raté | Tu as critiqué le retriever par mots-clés (juste), mais pas le tri. |
| 5 | Question de l'utilisateur écrite dans le prompt système | ❌ Raté | Tu as cité l'injection de prompt en général, sans la relier à ce code. |
| 8 | La mémoire est effacée à chaque question | ❌ Raté | Tu as vu « en mémoire », pas qu'elle est recréée à chaque appel. |
| 10 | La chaîne est reconstruite à chaque question | ❌ Raté | |
| 11 | Tous les utilisateurs partagent la même conversation | ❌ Raté | **Le plus grave** : un collaborateur peut voir l'historique d'un autre (données personnelles). |

**Bilan : 4 / 4 plantages corrigés (dont 3 avec l'outil), 0 / 8 erreurs silencieuses corrigées, 2 repérées en lecture (modèle et réglages, consigne de réponse).**

## Où ta correction du chunk est à revoir

Ta correction (`chunk_size=20`, `chunk_overlap=10`) supprime le plantage mais crée un problème de qualité :

| Point | Explication |
|---|---|
| Unité | Dans cet outil, la taille se compte par défaut en **caractères**, pas en tokens. Je t'avais demandé comment le vérifier : réponse = la documentation de l'outil. |
| Effet | 20 caractères, c'est une demi-phrase. Le texte est coupé en petits morceaux et le chatbot reçoit des fragments inutilisables. |
| Overlap | 10 sur 20 = 50 %. Tu avais pourtant dit « 10 à 20 % » en lisant le code. |

À dire en entretien : « Le texte fait quelques lignes : pour un POC, je ne découpe pas, ou je prends des chunks de 200 caractères avec 20-30 de recouvrement. »

## Bonnes habitudes à reproduire

- **Lire avant de lancer et prédire** ce qui va arriver : tu l'as fait, et tu avais raison.
- **Poser une hypothèse avant de demander la correction.**
- **Relire dans l'éditeur** chaque changement de l'outil : excellent réflexe.
- **Dire « je ne comprends pas »** plutôt que de faire semblant.
- **Penser « client » et « prod »** : jeu de test, évaluation avant mise en prod.
- **Poser la question du cadre** en début d'entretien : « Puis-je m'appuyer sur un assistant de code ? »

## À corriger

1. **Répondre à la question posée, en une phrase**, avant d'expliquer la méthode.
2. **Expliquer chaque erreur avec tes mots** après la correction : « Le prompt attendait `question`, la chaîne envoyait `input` : les deux ne parlaient pas la même langue. »
3. **Contrôler la liste de l'outil** : lui demander « qu'est-ce qui ne plante pas mais reste faux ? » ; relire pour la sécurité, les données personnelles et les secrets.
4. **Demander un indice** quand tu bloques, sans attendre.
5. **Classer les erreurs en 3 familles** : plante / faux sans planter / risque de prod.
6. **Respecter le temps** : 25 minutes, c'est strict.

## Exercices pour t'entraîner

1. **Audit sans corriger (10 min).** Relis `chatbot_bugge.py` en ne cherchant que les erreurs silencieuses. Pour chacune, écris : *symptôme / cause probable / risque pour le client*. Sans toucher au code.
2. **Tableau des noms (5 min).** Dessine qui envoie et qui attend `input`, `question`, `history`, `chat_history`, `context`. À savoir expliquer en 30 secondes.
3. **Test d'une ligne.** Pour le bug des sessions partagées : « deux utilisateurs différents posent une question, puis je vérifie que leurs historiques sont séparés ». À dire à voix haute.
4. **Checklist de 6 questions** à te poser sur tout chatbot : où sont les secrets ? qui partage la mémoire ? que reçoit le modèle comme contexte ? que se passe-t-il hors sujet ? quel modèle, quels réglages ? comment je le vois en prod ?
5. **LangSmith.** Active le suivi sur ce chatbot et regarde le contexte réellement envoyé : c'est comme ça qu'on voit le tri à l'envers en 10 secondes. Priorité, puisque tu as annoncé maîtriser cet outil.
6. **Rejouer plus tard** : copie ton fichier modifié, remets l'original, et refais 20 minutes en commençant par la lecture complète et la liste en 3 familles.

## Phrases utiles

- « Avant de commencer : puis-je m'appuyer sur un assistant de code ? »
- « Je vais d'abord lire, classer ce qui plante et ce qui ne plante pas, puis corriger un point à la fois. »
- « Ça ne plante plus, mais je veux vérifier que le comportement est correct. »
- « Je ne le vois pas sans l'outil. Voici comment je procéderais : lancer, lire l'erreur, comparer ce qui est attendu et ce qui est reçu. »
- « Avant la prod : traces LangSmith, jeu de test du client, revue sécurité (secrets, données personnelles). »
