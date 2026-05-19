from pydantic import BaseModel
from typing import Optional


class ReviewDecision(BaseModel):
    reviewer_name: str
    decision: str
    reviewer_notes: Optional[str] = None
    edited_summary: Optional[str] = None