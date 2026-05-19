from datetime import datetime

from backend.database import SessionLocal
from backend.models.audit_log import AuditLog


def get_pending_reviews():

    db = SessionLocal()

    try:
        return db.query(AuditLog).filter(
            AuditLog.review_status == "PENDING"
        ).all()

    finally:
        db.close()

from datetime import datetime

from backend.database import SessionLocal
from backend.models.audit_log import AuditLog


def review_case(
    case_id: int,
    reviewer_name: str,
    decision: str,
    reviewer_notes: str = None,
    edited_summary: str = None
):
    db = SessionLocal()

    case = db.query(AuditLog).filter(
        AuditLog.id == case_id
    ).first()

    if not case:
        return None

    case.review_status = decision.upper()
    case.reviewer_notes = reviewer_notes
    case.reviewed_at = datetime.utcnow()

    if edited_summary:
        case.edited_summary = edited_summary

    db.commit()
    db.refresh(case)

    return case

def update_review_status(
    record_id: int,
    status: str,
    reviewer_notes: str = None,
    edited_summary: str = None
):

    db = SessionLocal()

    try:

        record = db.query(AuditLog).filter(
            AuditLog.id == record_id
        ).first()

        if not record:
            return None

        record.review_status = status
        record.reviewer_notes = reviewer_notes
        record.edited_summary = edited_summary
        record.reviewed_at = datetime.utcnow()

        db.commit()

        return record

    finally:
        db.close()