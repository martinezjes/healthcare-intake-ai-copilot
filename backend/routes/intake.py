from fastapi import APIRouter, Depends

from backend.models.intake_models import (
    IntakeRequest,
    IntakeResponse,
    IntakeAnalysis
)

from backend.services.ai_service import (
    generate_intake_analysis
)

from backend.services.audit_service import (
    save_audit_log
)

from backend.services.deps import get_current_user

router = APIRouter(
    prefix="/intake",
    tags=["Intake"]
)


@router.post(
    "/analyze",
    response_model=IntakeResponse
)
def analyze_intake(
    request: IntakeRequest,
    current_user=Depends(get_current_user)
):
    ai_response = generate_intake_analysis(
        request.intake_text
    )

    validated_analysis = IntakeAnalysis(
        **ai_response
    )

    save_audit_log(
        patient_id=request.patient_id,
        intake_text=request.intake_text,
        analysis=validated_analysis
    )

    return IntakeResponse(
        patient_id=request.patient_id,
        analysis=validated_analysis
    )