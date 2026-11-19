# Architecture

```mermaid
flowchart LR
    Dev[Developer] --> Git[GitHub Repository]
    Git --> GHA[GitHub Actions CI]
    GHA --> Test[Pytest]
    GHA --> Docker[Docker Build]
    Docker --> GHCR[GitHub Container Registry]
    GHCR --> K8s[Kubernetes Deployment]
    User[Verifier] --> App[FastAPI Order Service]
    K8s --> App
```

## Components

- `app/main.py` hosts the FastAPI order service.
- `tests/test_main.py` validates the API responses.
- `Dockerfile` builds a non-root container image.
- `.github/workflows/ci.yml` runs tests, builds the image, performs a smoke test, and publishes to GHCR on `main`.
- `k8s/` contains Kubernetes deployment manifests.
