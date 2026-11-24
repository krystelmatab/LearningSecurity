# Préparation entretien technique — Consultante IA chez SFEIR

## Ce qu'on sait de la façon dont SFEIR évalue

- Le processus technique historique s'appelle les **« PlayOffs »** : plusieurs tests techniques menés par des **consultants SFEIR en pair programming** (pas des RH). Les retours Glassdoor disent la même chose : **ils valorisent le raisonnement** plus que la bonne réponse.
- Un évaluateur SFEIR décrit l'exercice comme **« un échange entre développeurs plus qu'une évaluation »**. → Traite l'évaluateur comme un collègue avec qui tu travailles sur le problème d'un client.
- SFEIR recommande d'être à l'aise avec les **outils de collaboration** (partage d'écran, VS Code Live Share). → Teste ta visio, ton partage d'écran et un environnement Python qui marche **avant** l'entretien.
- **SFEIR Institute forme sur Claude / Claude Code** et SFEIR est partenaire Google Cloud → l'exercice de prompting avec Claude est très plausible ; Vertex AI / Gemini peut apparaître dans les questions d'architecture.

Ton positionnement à tenir pendant toute l'heure :
> « Je suis consultante : je cadre, je conçois et je prototype. Je ne suis pas développeuse de métier, mais je sais lire du code, le débugger, et construire un POC fonctionnel avec LangChain. »

Ça rend chaque exercice cohérent : sur le code, tu montres la **méthode** et la **vision prod** (sécurité, données, éval), pas la vitesse de frappe.

## Le contenu du dossier

| Dossier | Contenu |
|---|---|
| `partie2-prompting/` | 5 exercices de prompting réalistes + `playground.py` pour les tester |
| `partie3-langchain/` | 2 programmes buggés qui tournent vraiment : `chatbot_bugge.py` (RAG + mémoire, 11 bugs) et `extracteur_bugge.py` (structured output, 8 bugs) |
| `langsmith/` | Guide express + `demo_eval.py` (dataset, évaluateurs, experiment) |
| `corriges/` | ⚠️ **Ne pas ouvrir avant d'avoir fait la simulation correspondante** |

## Le programme sur 2 jours

### Jour 1 — Apprendre en faisant

| Créneau | Activité | Durée |
|---|---|---|
| Matin | 🎙 **Simulation 1** avec Claude : prompting P1 + P2 | 45 min |
| | Débrief + lecture `corriges/partie2_corriges.md` (P1, P2) | 30 min |
| Midi | Installer l'environnement : `pip install -r partie3-langchain/requirements.txt` | 15 min |
| Après-midi | 🎙 **Simulation 2** : debugging `chatbot_bugge.py` | 45 min |
| | Débrief + `corriges/partie3_bugs.md` — refaire seule les bugs ratés | 45 min |
| Fin de journée | **LangSmith** : suivre `langsmith/GUIDE.md` de bout en bout (compte, traces, dataset, experiment) | 2 h |

### Jour 2 — Conditions réelles

| Créneau | Activité | Durée |
|---|---|---|
| Matin | 🎙 **Simulation 3** : prompting P3 + P4, puis debugging `extracteur_bugge.py` | 60 min |
| | Débrief | 30 min |
| Après-midi | 🎙 **Simulation 4 — entretien blanc complet de 60 min** : intro, questions éclair, un exercice de prompting **inédit**, un debugging **inédit** (Claude l'écrit en direct, tu ne l'as jamais vu) | 60 min |
| | Débrief final + fiche « mes 5 points d'attention » | 30 min |
| Soir | Relire uniquement les phrases clés ci-dessous. Rien de nouveau. | 20 min |

## Comment se déroule une simulation avec Claude

1. Tu écris dans la conversation : **« Simulation 1 »** (ou 2, 3, 4).
2. Claude joue l'évaluateur SFEIR : il présente le contexte client, te donne l'énoncé, te relance, refuse de te donner la solution, mais te donne un indice si tu le demandes (comme en vrai).
3. **Tu « penses à voix haute » par écrit** : écris ton raisonnement, pas seulement ta réponse. Astuce : utilise la dictée vocale de ton téléphone/ordinateur pour être proche de l'oral.
4. Pour le code : modifie les fichiers chez toi, colle la stacktrace ou ton diff dans la conversation.
5. À la fin, tape **« Fin »** : Claude sort de son rôle et te donne une évaluation avec la grille SFEIR (méthode, communication, profondeur, vision prod, collaboration) et une note /5 par critère.

## Phrases clés (à avoir en bouche)

**Pour démarrer un exercice**
- « Avant de me lancer, je reformule pour être sûre d'avoir compris : … C'est bien ça ? »
- « J'ai deux ou trois questions sur le contexte : qui consomme la sortie ? quel volume ? »

**Pendant**
- « Mon hypothèse est … ; je vais la vérifier en … »
- « Je vois deux options : A, plus simple, B, plus robuste. Pour un POC je partirais sur A, en prod sur B. »
- « Là je bloque sur la syntaxe exacte ; l'idée, c'est … Tu me confirmes ou je vérifie dans la doc ? »

**Quand ça tourne**
- « Ça ne plante plus, mais je veux vérifier que le comportement est correct. »

**Pour conclure**
- « En résumé, j'ai trouvé X problèmes : … Avant une mise en prod, j'ajouterais : traces LangSmith, un dataset d'évaluation, et une revue sécurité. »

## Questions à poser à ton évaluateur (partie intro)

- « Sur les missions IA en cours, quelle est la part cadrage / conseil vs build ? »
- « Comment se passe la montée en compétence chez SFEIR (SFEIR Institute, certifications, communautés internes) ? »
- « Quels sont les cas d'usage GenAI que vous voyez le plus chez les clients en ce moment ? »
- « Qu'est-ce qui distingue un consultant IA qui réussit chez SFEIR ? »
- « Qu'est-ce que tu aimes le plus dans ton quotidien chez SFEIR ? »

## Sources

- [Avis Glassdoor — processus d'entretien SFEIR](https://www.glassdoor.com/Interview/Sfeir-Interview-Questions-E737728.htm)
- [Glassdoor — SFEIR Paris](https://www.glassdoor.ie/Interview/Sfeir-Paris-Interview-Questions-EI_IE737728.0,5_IL.6,11_IM1080.htm)
- [Glassdoor — SFEIR Developer](https://www.glassdoor.com/Interview/Sfeir-Developer-Interview-Questions-EI_IE737728.0,5_KO6,15.htm)
- [Indeed — entretiens SFEIR](https://fr.indeed.com/cmp/Sfeir/interviews)
- [SFEIR Institute — Claude Code interview questions](https://institute.sfeir.com/en/claude-code/claude-code-resources/interview/)
- [Article SFEIR sur Medium (Codeshake)](https://medium.com/codeshake/sfeir-vous-livre-ses-tips-et-astuces-pour-pr%C3%A9parer-au-mieux-vos-entretiens-techniques-358f22385db2) — non lisible depuis cet environnement : à lire toi-même.
- [Exponent — process LangChain Deployed Engineer](https://www.tryexponent.com/guides/langchain-deployed-engineer-interview)
