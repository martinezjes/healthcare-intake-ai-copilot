def generate_intake_analysis(intake_text: str):
    """
    Mock AI service for development.
    Simulates LLM output without external API dependency.
    """

    text = intake_text.lower()

    symptoms = []

    if "chest pain" in text:
        symptoms.append("chest pain")

    if "dizziness" in text:
        symptoms.append("dizziness")

    if "shortness of breath" in text:
        symptoms.append("shortness of breath")

    # Default logic
    urgency = "low"
    escalation = False
    routing = "Primary Care Review"
    confidence = 0.85

    # Risk logic (simulated clinical heuristics)
    if "chest pain" in symptoms:
        urgency = "high"
        escalation = True
        routing = "Emergency Department Review"
        confidence = 0.93

    elif "shortness of breath" in symptoms:
        urgency = "medium"
        routing = "Urgent Care Review"
        confidence = 0.88

    summary = (
        "Patient presents with reported symptoms requiring clinical review. "
        "No AI model was used (mock mode active)."
    )

    follow_up = (
        "Your intake has been received and is being reviewed by our clinical team."
    )

    return {
        "summary": summary,
        "extracted_symptoms": symptoms,
        "urgency_level": urgency,
        "routing_recommendation": routing,
        "escalation_required": escalation,
        "confidence_score": confidence,
        "follow_up_message": follow_up
    }