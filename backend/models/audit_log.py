from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from datetime import datetime

from backend.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    patient_id = Column(String)

    intake_text = Column(String)

    summary = Column(String)

    urgency_level = Column(String)

    routing_recommendation = Column(String)

    confidence_score = Column(Float)

    escalation_required = Column(Boolean)

    # NEW — HUMAN REVIEW WORKFLOW
    review_status = Column(String)
    reviewer_notes = Column(String, nullable=True)
    edited_summary = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)
    reviewed_at = Column(DateTime, nullable=True)