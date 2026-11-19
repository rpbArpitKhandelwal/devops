# DevOps CI/CD and Kubernetes Deployment Lab

A hands-on DevOps portfolio project that packages a small FastAPI order service with automated tests, containerization, CI/CD, GHCR publishing, and Kubernetes deployment manifests.

## Problem Statement

Build a simple, verifiable service that demonstrates core DevOps skills: Python service packaging, automated testing, Docker image creation, CI validation, GHCR publishing, and Kubernetes deployment preparation.

## Technology Stack

- Python 3.13
- FastAPI
- Pytest
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)
- Kubernetes
- kind

## Architecture

```mermaid
flowchart LR
    Dev[Developer] --> Git[GitHub Repository]
    Git --> GHA[GitHub Actions CI]
    GHA --> Test[Pytest]
    GHA --> Docker[Docker Build]
    Docker --> GHCR[GHCR Publish]
    GHCR --> K8s[Kubernetes Cluster]
    K8s --> API[FastAPI Order Service]
    User --> API
```

## Repository Structure

```text
.
├── .github/workflows/ci.yml
├── app/main.py
├── docs/
│   ├── architecture.md
│   ├── troubleshooting.md
│   ├── runbook.md
│   └── evidence/
├── k8s/
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   └── service.yaml
├── tests/
│   ├── conftest.py
│   └── test_main.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── pytest.ini
└── requirements.txt
```

## Local Setup

1. Create the virtual environment if needed: `py -m venv .venv`
2. Install dependencies: `./.venv/Scripts/python.exe -m pip install -r requirements.txt`
3. Start the API: `./.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000`
4. Open docs: `http://127.0.0.1:8000/docs`

## Running Tests

- `./.venv/Scripts/python.exe -m pytest -v`

## Docker

- Build: `docker build -t devops-cicd-kubernetes-lab:local .`
- Run: `docker run --rm -d --name order-service -p 8000:8000 devops-cicd-kubernetes-lab:local`
- Verify root: `curl http://127.0.0.1:8000/`
- Verify health: `curl http://127.0.0.1:8000/health`
- Verify orders: `curl http://127.0.0.1:8000/orders`

## GitHub Actions Pipeline

The workflow in `.github/workflows/ci.yml` performs:

1. Source checkout
2. Python setup
3. Dependency installation
4. Pytest execution
5. Docker image build
6. Container smoke test
7. GHCR push on `main`

Successful run:

- `https://github.com/rpbArpitKhandelwal/devops/actions/runs/44516038848`

## GHCR Image Information

Published image path:

- `ghcr.io/rpbarpitkhandelwal/devops-cicd-kubernetes-lab:latest`

Pull command:

- `docker pull ghcr.io/rpbarpitkhandelwal/devops-cicd-kubernetes-lab:latest`

## Kubernetes Deployment

1. Ensure a Kubernetes context is active.
2. Apply manifests: `kubectl apply -k k8s`
3. Port-forward: `kubectl port-forward svc/order-service 8000:80`
4. Verify endpoints from `http://127.0.0.1:8000`

The default manifest already points at the published GHCR image.

## Verification Commands

- API tests: `./.venv/Scripts/python.exe -m pytest -v`
- Docker logs: `docker logs order-service`
- Kubernetes render: `kubectl kustomize k8s`
- Kubernetes pods: `kubectl get pods`
- Kubernetes service: `kubectl get svc order-service`

## Troubleshooting

- Architecture notes: `docs/architecture.md`
- Troubleshooting log: `docs/troubleshooting.md`
- Operations runbook: `docs/runbook.md`
- Verification notes: `docs/evidence/verification.md`

## Screenshots and Evidence

Store genuine screenshots of successful local runs, Docker output, CI runs, and Kubernetes verification in `docs/evidence/`.

## Current Verification Status

- Local pytest verification: completed
- Live local FastAPI verification: completed
- Docker build and container smoke test: completed
- GHCR image pull and run verification: completed
- Kubernetes manifest render: completed
- Live Kubernetes deployment on kind: completed
- GitHub Actions CI run: completed successfully
