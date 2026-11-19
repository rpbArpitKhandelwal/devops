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
- `docker pull ghcr.io/rpbarpitkhandelwal/devops-cicd-kubernetes-lab:latest` completed successfully.
- `docker run -d --name ghcr-order-service -p 8002:8000 ghcr.io/rpbarpitkhandelwal/devops-cicd-kubernetes-lab:latest` served `/health` and `/orders` successfully.
- GitHub Actions run `44516038848` completed successfully.
- `kubectl kustomize k8s` rendered the manifests successfully.
- kind cluster `kind-devops-lab` deployed the app successfully.
- `kubectl port-forward svc/order-service 8003:80` exposed a live service where `/`, `/health`, `/orders`, and `/docs` all responded successfully.

## Published links

- Repository: `https://github.com/rpbArpitKhandelwal/devops`
- Actions run: `https://github.com/rpbArpitKhandelwal/devops/actions/runs/44516038848`
- GHCR image: `ghcr.io/rpbarpitkhandelwal/devops-cicd-kubernetes-lab:latest`
