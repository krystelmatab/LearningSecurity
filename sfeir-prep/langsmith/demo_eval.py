"""
Démo LangSmith : dataset + évaluateurs + experiment.
Nécessite LANGSMITH_API_KEY. Fonctionne sans clé Anthropic (on évalue une fonction simple).

    python demo_eval.py
"""

from langsmith import Client, traceable

client = Client()
DATASET = "sfeir-prep-rh"

EXEMPLES = [
    ("Combien de jours de télétravail par semaine ?", "3"),
    ("Quel est le budget formation annuel ?", "2000"),
    ("Combien de RTT par an ?", "10"),
    ("Puis-je télétravailler en période d'essai ?", "non"),
]

if not client.has_dataset(dataset_name=DATASET):
    ds = client.create_dataset(DATASET, description="Questions RH de référence")
    client.create_examples(
        dataset_id=ds.id,
        inputs=[{"question": q} for q, _ in EXEMPLES],
        outputs=[{"attendu": a} for _, a in EXEMPLES],
    )


@traceable(name="faux_chatbot_rh")
def chatbot(inputs: dict) -> dict:
    """Remplace-le par ta vraie chaîne : chain.invoke({'input': inputs['question']})"""
    q = inputs["question"].lower()
    if "télétravail" in q and "essai" in q:
        return {"reponse": "Non, pas pendant la période d'essai."}
    if "télétravail" in q:
        return {"reponse": "Jusqu'à 3 jours par semaine."}
    if "formation" in q:
        return {"reponse": "Le budget est de 2000 euros par an."}
    return {"reponse": "Je ne sais pas."}  # erreur volontaire sur les RTT


def contient_attendu(outputs: dict, reference_outputs: dict) -> bool:
    """Évaluateur 'code' : la réponse contient-elle la valeur attendue ?"""
    return reference_outputs["attendu"].lower() in outputs["reponse"].lower()


def pas_de_je_ne_sais_pas(outputs: dict) -> bool:
    return "je ne sais pas" not in outputs["reponse"].lower()


resultats = client.evaluate(
    chatbot,
    data=DATASET,
    evaluators=[contient_attendu, pas_de_je_ne_sais_pas],
    experiment_prefix="v1-regles",
)
print("Experiment lancée — ouvre LangSmith > Datasets & Experiments >", DATASET)
