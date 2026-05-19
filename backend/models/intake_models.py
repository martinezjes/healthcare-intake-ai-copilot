from pydantic import BaseModel
from typing import List


class IntakeRequest(BaseModel):
    patient_id: str
    intake_text: str
    source: str


class IntakeAnalysis(BaseModel):
    summary: str
    extracted_symptoms: List[str]
    urgency_level: str
    routing_recommendation: str
    escalation_required: bool
    confidence_score: float
    follow_up_message: str


class IntakeResponse(BaseModel):
    patient_id: str
    analysis: IntakeAnalysis