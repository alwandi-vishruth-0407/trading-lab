# Trading Lab

A project for learning full stack development by building an educational paper trading application with virtual money and guided practice.

## Current implementation

The application currently contains one FastAPI endpoint: `GET /health`.

```json
{"status": "ok", "service": "Trading Lab API"}
```

Trading, accounts, market data, portfolios, and the frontend are planned features. They are not implemented yet. See [the product specification](docs/PRODUCT_SPEC.md) for the intended scope.

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
| `docs/` | Product specification and learning notes |
| `docs/pdf/` | PDF generation tools and teaching example checks |
| `docs/video/` | Narrated demo generation and verification tools |
| `output/pdf/` | Printable learning references |
| `output/video/` | Narrated demo, transcript, captions, and chapters |

## Learning references

* [First API lesson](docs/LESSON_01_FIRST_API.md)
* [Detailed FastAPI explanation](docs/LESSON_01_FASTAPI_EXPLAINED.md)
* [Printable FastAPI guide](output/pdf/Trading_Lab_Lesson_01_FastAPI_Explained.pdf)
* [Narrated demo](output/video/Trading_Lab_FastAPI_Demo.mp4)
* [Demo transcript](output/video/Trading_Lab_FastAPI_Demo_Transcript.md)

The media generation scripts are authoring tools with additional local dependencies, including Windows fonts, speech synthesis, and FFmpeg for the video. They are not required to run the API. Some learning references retain the original author's local paths; substitute your own checkout location when following them.

Virtual environments, downloaded tools, temporary output, and unrelated local work are excluded from Git. The next planned application increment introduces a path parameter, followed by a fictional instrument lookup.
