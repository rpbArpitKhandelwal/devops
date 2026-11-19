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
