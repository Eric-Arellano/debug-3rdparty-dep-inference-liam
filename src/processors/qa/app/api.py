from typing import List

from app.qa import QAHandler
from fastapi import BackgroundTasks, FastAPI, HTTPException
from starlette.responses import RedirectResponse


qa_handler = QAHandler()

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
    """Returns a health message for the QA service."""
    return {"status": "healthy"}

# REDACTED