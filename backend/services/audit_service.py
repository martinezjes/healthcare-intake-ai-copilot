from backend.database import SessionLocal

from backend.models.audit_log import AuditLog


def save_audit_log(
    patient_id,
    intake_text,
    analysis
):

    db = SessionLocal()

    try:

        audit_entry = AuditLog(
            patient_id=patient_id,
            intake_text=intake_text,
            summary=analysis.summary,
            urgency_level=analysis.urgency_level,
            routing_recommendation=(
                analysis.routing_recommendation
            ),
            confidence_score=(
                analysis.confidence_score
            ),
            escalation_required=(
                analysis.escalation_required
            )
        )

        db.add(audit_entry)

        db.commit()

    finally:

        db.close()