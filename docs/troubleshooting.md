# Troubleshooting

## 1. Broken Python command

- **Problem:** `python -m pytest -v` failed in PowerShell.
- **Observed error:** `The term 'python' is not recognized as the name of a cmdlet...`
- **Investigation commands:** `where.exe python`, `where.exe py`, `./.venv/Scripts/python.exe --version`
- **Root cause:** `python` was not on `PATH` for this shell, while the local virtual environment interpreter existed.
- **Fix applied:** Switched all project commands to `./.venv/Scripts/python.exe`.
- **Verification:** `./.venv/Scripts/python.exe -m pytest -v` collected and ran tests.
- **Learning:** Always verify which interpreter is active before installing packages or running tests.

## 2. Stale SSL certificate configuration

- **Problem:** pip initially failed before dependencies were installed.
- **Observed error:** `invalid path: C:\Program Files\PostgreSQL\18\ssl\certs\ca-bundle.crt`
- **Investigation commands:** `Get-ChildItem Env:`, `Test-Path 'C:\Program Files\PostgreSQL\18\ssl\certs\ca-bundle.crt'`
- **Root cause:** A stale `CURL_CA_BUNDLE` user environment variable pointed to a deleted PostgreSQL CA bundle.
- **Fix applied:** Removed the bad user-level `CURL_CA_BUNDLE` override and re-ran installation with the virtual environment interpreter.
- **Verification:** `./.venv/Scripts/python.exe -m pip install -r requirements.txt` completed successfully.
- **Learning:** Broken global SSL overrides can affect otherwise healthy Python environments.

## 3. GitHub Actions import failure on Linux

- **Problem:** the first successful local setup still failed in GitHub Actions.
- **Observed error:** `ModuleNotFoundError: No module named 'app'`
- **Investigation commands:** local Windows pytest run, Linux reproduction with `docker run --rm -v ${PWD}:/workspace -w /workspace python:3.13-slim bash -lc "pip install -r requirements.txt && pytest -v"`
- **Root cause:** the repository root was not guaranteed to be on `sys.path` during Linux test collection.
- **Fix applied:** Added `tests/conftest.py` to prepend the project root before tests import `app.main`.
- **Verification:** local Windows tests passed, Linux container reproduction passed, and GitHub Actions run `44516038848` succeeded.
- **Learning:** A test suite that works on one OS can still fail in CI if imports depend on environment-specific path behavior.

## 4. Kubernetes context unavailable by default

- **Problem:** `kubectl` was installed but no active cluster context existed.
- **Observed error:** `current-context is not set` and `Unable to connect to the server: dial tcp [::1]:8080...`
- **Investigation commands:** `kubectl config current-context`, `kubectl cluster-info`
- **Root cause:** there was no running local cluster behind the default context.
- **Fix applied:** Installed a workspace-local `kind` binary, created the `kind-devops-lab` cluster, and deployed the app there.
- **Verification:** `kubectl rollout status deployment/order-service` completed successfully and the service responded through `kubectl port-forward`.
- **Learning:** Having `kubectl` installed is separate from having a live cluster to talk to.

## 5. Controlled troubleshooting exercise: wrong container port mapping

- **Problem:** The container was intentionally started with `-p 8001:9000`.
- **Observed error:** `The underlying connection was closed: The connection was closed unexpectedly.`
- **Investigation commands:** `docker run -d --name order-service-bad -p 8001:9000 devops-cicd-kubernetes-lab:local`, `docker ps --filter name=order-service-bad`, `docker logs order-service-bad`
- **Root cause:** The app listens on container port `8000`, but the host was mapped to container port `9000`.
- **Fix applied:** Switched to `docker run -p 8000:8000 devops-cicd-kubernetes-lab:local`.
- **Verification:** After correcting the mapping, `/`, `/health`, and `/orders` all returned successful responses.
- **Learning:** When host requests fail but container logs show the app is healthy, confirm the published container port first.
