from datetime import datetime, timezone

from fastapi import FastAPI

APP_NAME = "DevOps CI/CD and Kubernetes Deployment Lab"

app = FastAPI(
    title=APP_NAME,
    version="1.0.0",
    description="Sample e-commerce order service for DevOps portfolio verification.",
)

SAMPLE_ORDERS = [
    {"id": 1, "item": "Laptop", "status": "shipped"},
    {"id": 2, "item": "Keyboard", "status": "processing"},
]


@app.get("/")
def home() -> dict[str, str]:
    return {
        "application": APP_NAME,
        "status": "success",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/orders")
def get_orders() -> dict[str, object]:
    return {
        "orders": SAMPLE_ORDERS,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
