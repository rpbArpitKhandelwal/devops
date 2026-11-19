from fastapi import FastAPI

APP_NAME = "DevOps CI/CD and Kubernetes Deployment Lab"

app = FastAPI(title=APP_NAME, version="1.0.0")


@app.get("/")
def home() -> dict[str, str]:
    return {
        "application": APP_NAME,
        "status": "success",
    }
