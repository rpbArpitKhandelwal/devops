# Verification Notes

## Verified locally on 2026-11-19

- `./.venv/Scripts/python.exe -m pytest -v` passed with `3 passed`.
- `./.venv/Scripts/python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000` served:
  - `GET /` returning `{"application":"DevOps CI/CD and Kubernetes Deployment Lab","status":"success"}`
  - `GET /health` returning `{"status":"healthy"}`
  - `GET /orders` returning sample orders with a UTC timestamp
  - `GET /docs` returning HTTP `200`
- `docker build -t devops-cicd-kubernetes-lab:local .` completed successfully.
- `docker run -d --name order-service -p 8000:8000 devops-cicd-kubernetes-lab:local` served `/`, `/health`, and `/orders` successfully.
- `kubectl kustomize k8s` rendered the manifests successfully.

## Pending external verification

- GitHub Actions successful run URL
- Published GHCR image URL
- Live Kubernetes deployment verification after a cluster context is configured
- Screenshot capture into `docs/evidence/`
