from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.services.deps import get_current_user
from backend.services.rbac import require_admin
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
def fetch_all_logs(
    limit: int = 50,
    offset: int = 0,
    urgency: str = None,
    db: Session = Depends(get_db),
    admin_user=Depends(require_admin)
):
    logs = get_all_logs(
        db,
        limit=limit,
        offset=offset,
        urgency=urgency
    )

    return {
        "limit": limit,
        "offset": offset,
        "urgency_filter": urgency,
        "count": len(logs),
        "logs": logs
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

    return {
        "patient_id": patient_id,
        "limit": limit,
        "offset": offset,
        "count": len(logs),
        "logs": logs
    }