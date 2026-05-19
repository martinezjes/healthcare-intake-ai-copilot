from fastapi import APIRouter

from backend.services.review_service import (
    get_pending_reviews,
    update_review_status
)

router = APIRouter(prefix="/review", tags=["Review"])


@router.get("/pending")
def pending_reviews():

    return get_pending_reviews()


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