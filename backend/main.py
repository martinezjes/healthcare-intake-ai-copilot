from fastapi import FastAPI
from backend.routes import health, intake

app = FastAPI(
    title="Healthcare Intake AI Copilot",
    version="1.0.0"
)

app.include_router(health.router)
app.include_router(intake.router)


@app.get("/")
def root():
    return {
        "message": "Healthcare Intake AI Copilot API is running"
    }