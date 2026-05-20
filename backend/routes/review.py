from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from backend.utils.api_response import api_response

from backend.database import SessionLocal
from backend.services.deps import get_current_user
from backend.services.rbac import require_admin
from backend.utils.response import success_response
from backend.services.review_service import get_logs_by_patient
from backend.models.audit_log import AuditLog

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


# =========================
# ADMIN: All logs (paginated + optional urgency filter)
# =========================
@router.get("/logs")
def fetch_all_logs(
    limit: int = 10,
    offset: int = 0,
    urgency: str | None = Query(None),
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)  # enforce admin access
):
    query = db.query(AuditLog)

    # optional filter
    if urgency:
        query = query.filter(AuditLog.urgency_level == urgency)

    logs = query.limit(limit).offset(offset).all()

    return api_response(
    data={
        "logs": logs
    },
    message="Logs retrieved successfully",
    meta={
        "limit": limit,
        "offset": offset,
        "urgency_filter": urgency
    }
)


# =========================
# USER: Logs for specific patient
# =========================
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
            "offset": offset
        },
        message="Logs retrieved successfully"
    )