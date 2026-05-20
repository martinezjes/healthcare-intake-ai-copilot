from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.deps import get_current_user
from backend.services.rbac import require_admin
from backend.utils.response import success_response
from backend.services.review_service import (
    get_all_logs,
    get_logs_by_patient
)

router = APIRouter(
    prefix="/review",
    tags=["Review"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ADMIN ONLY: All logs with pagination + filtering
@router.get("/logs")
def fetch_patient_logs(
    limit: int = 10,
    offset: int = 0,
    urgency: str | None = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    query = db.query(...)  # your existing query logic here

    if urgency:
        query = query.filter(...)

    logs = query.limit(limit).offset(offset).all()

    return {
        "limit": limit,
        "offset": offset,
        "urgency_filter": urgency,
        "data": logs
    }


# AUTHENTICATED: Patient logs with pagination
@router.get("/logs/{patient_id}")
def fetch_patient_logs(
    patient_id: str,
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    logs = get_logs_by_patient(
        db,
        patient_id=patient_id,
        limit=limit,
        offset=offset
    )

    return success_response(
    data={
        "count": len(logs),
        "logs": logs
    },
    meta={
        "limit": limit,
        "offset": offset,
        "urgency_filter": urgency
    },
    message="Logs retrieved successfully"
)