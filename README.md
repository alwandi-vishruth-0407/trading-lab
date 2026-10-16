# Trading Lab

A project for learning full stack development by building an educational paper trading application with virtual money and guided practice.

## Current implementation

The application currently contains one FastAPI endpoint: `GET /health`.

```json
{"status": "ok", "service": "Trading Lab API"}
```

Trading, accounts, market data, portfolios, and the frontend are planned features. They are not implemented yet.

## Run locally on Windows

Open PowerShell in the repository root. Python must be installed. The existing development environment used Python 3.14.

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

Visit http://127.0.0.1:8000/health to see the response, or http://127.0.0.1:8000/docs for the interactive API documentation. Stop the server with Ctrl+C. This command runs a local development server.

## Repository contents

| Location | Purpose |
| --- | --- |
| `backend/` | Application code and Python dependency snapshot |

Virtual environments, local configuration, personal learning materials, and temporary output are excluded from Git.
