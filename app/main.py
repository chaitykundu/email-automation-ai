from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.email import router as email_router

app = FastAPI(
    title=settings.APP_NAME
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)
app.include_router(
    email_router,
    prefix="/api/v1",
    tags=["Email"]
)


@app.get("/")
def root():
    return {
        "message": "AI Email Automation System"
    }