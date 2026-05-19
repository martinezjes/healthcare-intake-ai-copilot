import json

from backend.utils.prompt_loader import load_prompt


def generate_intake_analysis(intake_text: str):

    prompt_template = load_prompt(
        "intake_extraction_prompt.txt"
    )

    final_prompt = prompt_template.format(
        intake_text=intake_text
    )

    # MOCK structured AI response
    # Later replaced with OpenAI call

    text = intake_text.lower()

    symptoms = []

    if "chest pain" in text:
        symptoms.append("chest pain")

    if "dizziness" in text:
        symptoms.append("dizziness")

    if "shortness of breath" in text:
        symptoms.append("shortness of breath")

    urgency = "low"
    escalation = False
    routing = "Primary Care Review"
    confidence = 0.82

    if "chest pain" in symptoms:
        urgency = "high"
        escalation = True
        routing = "Emergency Department Review"
        confidence = 0.95

    mock_response = {
        "summary": (
            "Patient intake processed successfully."
        ),
        "extracted_symptoms": symptoms,
        "urgency_level": urgency,
        "routing_recommendation": routing,
        "escalation_required": escalation,
        "confidence_score": confidence,
        "follow_up_message": (
            "Your intake has been received."
        )
    }

    return mock_response