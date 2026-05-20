from fastapi import FastAPI

from backend.routes.health import router as health_router
from backend.routes.intake import router as intake_router
from backend.routes.review import router as review_router
from backend.routes import auth
from backend.routes.user import router as users_router

app = FastAPI(
    title="Healthcare Intake AI Copilot",
    version="1.0.0"
)

# Routers
app.include_router(health_router)
app.include_router(intake_router)
app.include_router(review_router)
app.include_router(auth.router)
app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Healthcare Intake AI Copilot is running"}