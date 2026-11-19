# Runbook

## Local Python

- Create venv: `py -m venv .venv`
- Install deps: `./.venv/Scripts/python.exe -m pip install -r requirements.txt`
- Run app: `./.venv/Scripts/python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Run tests: `./.venv/Scripts/python.exe -m pytest -v`
