from os import getenv

from celery import Celery
from fastapi import BackgroundTasks, FastAPI
from starlette.responses import RedirectResponse

app = FastAPI(
    title="qa-inference",
    version="0.0.0",
    description="something here",
)

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse("/docs")


@app.get("/status", tags=["General"])
def read_status():
    """Returns a health message for the service."""
    return {"status": "healthy"}

# REDACTED CODE 