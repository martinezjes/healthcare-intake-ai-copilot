from sqlalchemy.orm import Session
from backend.models.audit_log import AuditLog


def get_all_logs(db: Session, limit: int = 50, offset: int = 0, urgency: str = None):
    query = db.query(AuditLog)

    # optional filtering by urgency inside JSON analysis
    if urgency:
        query = query.filter(AuditLog.analysis["urgency_level"].astext == urgency)

    return (
        query.order_by(AuditLog.id.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )


def get_logs_by_patient(db: Session, patient_id: str, limit: int = 50, offset: int = 0):
    return (
        db.query(AuditLog)
        .filter(AuditLog.patient_id == patient_id)
        .order_by(AuditLog.id.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )