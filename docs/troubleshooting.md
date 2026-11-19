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

## 3. Kubernetes cluster unavailable

- **Problem:** Kubernetes verification is blocked locally.
- **Observed error:** `current-context is not set` and `Unable to connect to the server: dial tcp [::1]:8080...`
- **Investigation commands:** `kubectl config current-context`, `kubectl cluster-info`, `kubectl kustomize k8s`
- **Root cause:** `kubectl` is installed, but no active cluster context is configured.
- **Fix applied:** Manifest files were created and rendered successfully with `kubectl kustomize k8s`; live deployment still requires enabling a cluster such as Docker Desktop Kubernetes.
- **Verification:** Client tooling is present and manifests render offline.
- **Learning:** Installed CLI tools do not guarantee an available runtime cluster.

## 4. Docker engine access

- **Problem:** Initial Docker commands failed from the agent sandbox.
- **Observed error:** `permission denied while trying to connect to the docker API at npipe:////./pipe/docker_engine`
- **Investigation commands:** `docker --version`, `docker info --format '{{.ServerVersion}}'`
- **Root cause:** The initial session lacked access to the Docker engine pipe.
- **Fix applied:** Re-ran Docker commands with approved host access and isolated Docker config under `.docker-tmp`.
- **Verification:** The image built successfully and the container served `/`, `/health`, and `/orders`.
- **Learning:** Docker Desktop being up does not guarantee pipe access from every execution context.

## 5. Controlled troubleshooting exercise: wrong container port mapping

- **Problem:** The container was intentionally started with `-p 8001:9000`.
- **Observed error:** `The underlying connection was closed: The connection was closed unexpectedly.`
- **Investigation commands:** `docker run -d --name order-service-bad -p 8001:9000 devops-cicd-kubernetes-lab:local`, `docker ps --filter name=order-service-bad`, `docker logs order-service-bad`
- **Root cause:** The app listens on container port `8000`, but the host was mapped to container port `9000`.
- **Fix applied:** Switched to `docker run -p 8000:8000 devops-cicd-kubernetes-lab:local`.
- **Verification:** After correcting the mapping, `/`, `/health`, and `/orders` all returned successful responses.
- **Learning:** When host requests fail but container logs show the app is healthy, confirm the published container port first.
