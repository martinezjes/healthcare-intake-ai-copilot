from pydantic import BaseModel, Field
from typing import List


class IntakeRequest(BaseModel):
    patient_id: str
    intake_text: str
    source: str = "web_form"


class IntakeAnalysis(BaseModel):
    summary: str
    extracted_symptoms: List[str]
    urgency_level: str
    routing_recommendation: str
    escalation_required: bool
    confidence_score: float
    follow_up_message: str