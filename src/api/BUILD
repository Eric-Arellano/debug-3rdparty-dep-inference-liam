python_requirements()

python_library(
    name="api",
    sources=["**/*.py"],
    interpreter_constraints=[">=3.6"],
    dependencies=[
        "src/api:celery", 
        "src/api:fastapi", 
        "src/api:uvicorn", 
        "src/api:pydantic"
    ]
)