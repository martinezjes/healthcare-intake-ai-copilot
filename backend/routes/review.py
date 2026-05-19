from fastapi import APIRouter

from backend.schemas.review import ReviewDecision
from backend.services.review_service import review_case

from backend.services.review_service import (
    get_pending_reviews,
    update_review_status
)

router = APIRouter(prefix="/review", tags=["Review"])


@router.get("/pending")
def pending_reviews():

    return get_pending_reviews()

@router.post("/{case_id}")
def submit_review(
    case_id: int,
    review: ReviewDecision
):
    updated_case = review_case(
        case_id=case_id,
        reviewer_name=review.reviewer_name,
        decision=review.decision,
        reviewer_notes=review.reviewer_notes,
        edited_summary=review.edited_summary
    )

    if not updated_case:
        return {"error": "Case not found"}

    return {
        "message": "Review submitted successfully",
        "case_id": updated_case.id,
        "review_status": updated_case.review_status
    }

@router.post("/update")
def update_review(
    record_id: int,
    status: str,
    reviewer_notes: str = None,
    edited_summary: str = None
):

    return update_review_status(
        record_id,
        status,
        reviewer_notes,
        edited_summary
    )