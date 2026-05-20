from pydantic import BaseModel


class IntakeCreate(BaseModel):
    patient_name: str
    symptoms: str

    medications: str | None = None
    allergies: str | None = None
    notes: str | None = None