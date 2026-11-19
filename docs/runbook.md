# Runbook

## Local Python

- Create venv: `py -m venv .venv`
- Install deps: `./.venv/Scripts/python.exe -m pip install -r requirements.txt`
- Run app: `./.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Run tests: `./.venv/Scripts/python.exe -m pytest -v`

## Docker

- Build image: `docker build -t devops-cicd-kubernetes-lab:local .`
- Run container: `docker run --rm -d --name order-service -p 8000:8000 devops-cicd-kubernetes-lab:local`
- Check logs: `docker logs order-service`
- Check health: `curl http://localhost:8000/health`
- Stop container: `docker rm -f order-service`

## Kubernetes

- Check context: `kubectl config current-context`
- Apply manifests: `kubectl apply -k k8s`
- Check pods: `kubectl get pods`
- Check service: `kubectl get svc order-service`
- Describe deployment: `kubectl describe deployment order-service`
- View logs: `kubectl logs deployment/order-service`
- Port-forward: `kubectl port-forward svc/order-service 8000:80`

## GitHub Actions

- Push branch: `git push origin <branch>`
- Open PR to trigger validation workflow.
- Merge to `main` to trigger GHCR publish.
