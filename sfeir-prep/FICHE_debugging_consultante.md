# Fiche — Debugging en entretien : le rôle de la consultante IA

> Une page à relire avant vendredi. Objectif : montrer ta **méthode** et ta **vision client**, pas la syntaxe.

## La phrase de départ

> « Avant de commencer : puis-je m'appuyer sur un assistant de code ? Je suis consultante : je lis, je cadre, je vérifie et je prototype. »

## Le déroulé en 5 temps (25 min)

| Temps | Ce que je fais | Ce que je dis |
|---|---|---|
| 1. Cadrer (2 min) | Je pose 3 questions | « Combien d'utilisateurs ? Quelles données ? « Ça ne marche plus », c'est un message d'erreur ou des réponses fausses ? » |
| 2. Lire (5 min) | Je lis **sans lancer**, je classe en 3 familles | « Ça va planter / ça tournera mais sera faux / risques de prod. » |
| 3. Lancer (8 min) | Un plantage à la fois, je lis le message **en entier** | « Le programme dit que… donc je suppose que… je vérifie en… » |
| 4. Vérifier (5 min) | Je ne m'arrête pas à « ça tourne » | « Ça ne plante plus, mais est-ce que le comportement est correct ? » |
| 5. Conclure (1 min) | Je résume par famille et je propose la suite | « J'ai trouvé X, je soupçonne Y, avant la prod j'ajouterais Z. » |

## Les 3 risques à toujours chercher (sans savoir programmer)

| Question à se poser | Ce que ça peut cacher |
|---|---|
| **Où sont les mots de passe et les clés ?** | Une clé secrète écrite dans le fichier : elle finit dans Git. |
| **Qui voit la conversation de qui ?** | Tous les utilisateurs partagent la même mémoire : fuite de données personnelles. |
| **Que dit-on au modèle quand il ne sait pas ?** | Pas de consigne : il invente. Sur les RH, c'est grave. |

Et aussi : le nom du modèle est-il le bon ? La température est-elle basse ? La réponse est-elle assez longue ?

## Comment lire une erreur sans être développeuse

1. Lis **le dernier message** de l'erreur : c'est lui qui dit ce qui s'est passé.
2. Repère les mots qui décrivent un **manque** (« missing », « no attribute », « larger than ») ou un **nom** (une variable, un type).
3. Traduis en une phrase : « il manque… », « deux endroits ne s'accordent pas sur… », « on demande à X quelque chose qu'il ne sait pas faire ».
4. Fais **une hypothèse** et propose un test.

## Quand je bloque

- « Là je bloque sur la syntaxe ; l'idée, c'est… »
- Je demande un **indice** (c'est bien vu, pas pénalisant).
- Je propose un **test** plutôt que de deviner.

## Quand l'assistant de code corrige

Je ne dis jamais « l'outil l'a fait ». Je dis : « l'assistant propose X. Je comprends que ça corrige Y. Je vérifie en relançant : le symptôme a disparu et le comportement est correct. »

## Avant la mise en production (à dire pour conclure)

- **Suivi** des échanges avec LangSmith : on voit le contexte réellement envoyé au modèle ;
- **Jeu de test** de 20 questions RH validé par le client ;
- **Test de séparation** : deux utilisateurs ne voient pas la conversation de l'autre ;
- **Revue sécurité** : secrets, données personnelles, injection de prompt ;
- **Retriever** : passer des mots-clés à une recherche par le sens (vector store).

## À ne pas faire

- Se précipiter : lancer avant d'avoir lu.
- Dépasser le temps.
- Corriger un faux problème en silence : on le dit.
- Répondre « je ne sais pas » sans proposer une piste.
