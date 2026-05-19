from backend.utils.prompt_loader import load_prompt
from backend.utils.logger import logger


def generate_intake_analysis(intake_text: str):

    try:

        prompt_template = load_prompt(
            "intake_extraction_prompt.txt"
        )

        confidence = 0.91

        escalation_required = (
            confidence < 0.75
            or "chest pain" in intake_text.lower()
        )

        logger.info(
            f"Processing intake: {intake_text}"
        )

        mock_response = {
            "summary": (
                "Patient reports chest pain and "
                "shortness of breath."
            ),
            "extracted_symptoms": [
                "chest pain",
                "shortness of breath"
            ],
            "urgency_level": "high",
            "routing_recommendation": (
                "Emergency Department"
            ),
            "escalation_required": escalation_required,
            "confidence_score": confidence,
            "follow_up_message": (
                "Your intake has been flagged "
                "for expedited clinical review."
            )
        }

        logger.info(
            f"AI analysis completed successfully."
        )

        return mock_response

    except Exception as error:

        logger.error(
            f"AI processing failed: {str(error)}"
        )

        return {
            "summary": (
                "Unable to generate summary."
            ),
            "extracted_symptoms": [],
            "urgency_level": "unknown",
            "routing_recommendation": (
                "Manual Review Required"
            ),
            "escalation_required": True,
            "confidence_score": 0.0,
            "follow_up_message": (
                "Your intake requires manual review."
            )
        }