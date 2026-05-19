from fastapi import APIRouter

from backend.models.intake_models import IntakeRequest
from backend.services.ai_service import generate_intake_analysis

router = APIRouter(
    prefix="/intake",
    tags=["Intake"]
)


@router.post("/analyze")
def analyze_intake(request: IntakeRequest):

    ai_result = generate_intake_analysis(request.intake_text)

    return {
        "patient_id": request.patient_id,
        "analysis": ai_result
    }