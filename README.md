# Finance Agent

AI-powered financial research web app that generates structured, citation-backed reports from a user query. The app uses a Flask backend with an `agno` research `Agent`, the `Groq` LLM, and tools for web search and article parsing to produce a comprehensive financial report.

## Features
- Query-driven financial research and report generation
- Uses `DuckDuckGo` for search and `Newspaper4k` for article extraction
- Structured output: Executive Summary, Findings, Impact, Outlook, Sources
- Simple, modern UI with report download
- Health check endpoint for quick diagnostics

## Project Structure
- `app.py`: Flask server, routes, and agent setup
- `templates/index.html`: Frontend UI (query input, results, download)
- `src/text_summarization/*`: Placeholder package for future components/utilities
- `Finance_agent.ipynb`: Notebook (not used by the web app directly)
- `.env`: Environment variables (optional, for local development)

## Architecture
- **Frontend**: HTML/CSS/JS served by Flask (`index.html`)
- **Backend**: Flask API (`/generate`) that instantiates an `agno.Agent` using `Groq` model `llama-3.3-70b-versatile`
- **Tools**: `DuckDuckGoTools` for search and `Newspaper4kTools` for article parsing
- **Output**: Markdown content structured into headline, sections, and source links

## Requirements
- Python 3.10+
- Packages: `flask`, `agno`, `groq`, `duckduckgo-search` (via `DuckDuckGoTools`), `newspaper4k`
- Environment variables:
	- `GROQ_API_KEY` (required for `/generate`)
	- `AGNO_API_KEY` (optional, used by `agno` if needed)

## Setup
1. Create and activate a virtual environment.
2. Install dependencies.
3. Set environment variables.
4. Run the app.

### Windows (PowerShell)
```powershell
# From the repo root
python -m venv venv
& .\venv\Scripts\Activate.ps1

# Install core dependencies
pip install flask agno groq duckduckgo-search newspaper4k

# Set environment variables for the session
$env:GROQ_API_KEY = "<your_groq_api_key>"
# Optional
$env:AGNO_API_KEY = "<your_agno_api_key>"

# Run Flask
python app.py
# or
$env:FLASK_APP = "app.py"; flask run
```

### Environment File (optional)
Create a `.env` and load it with your preferred method, or set variables in your shell profile. The app reads `GROQ_API_KEY` and `AGNO_API_KEY` from the environment.

## Usage
1. Open `http://localhost:5000` in your browser.
2. Enter a financial research query (e.g., "Analyze the impact of AI on banking").
3. Click "Generate Report".
4. Download the resulting markdown report if desired.

## API
- `GET /`: Serves the UI.
- `POST /generate`: Body `{ "query": "..." }` → returns `{ success, report | error }`.
- `GET /health`: Returns `{ status, groq_api_key_set, agno_api_key_set }`.

## Agent Configuration
Defined in `app.py` via `create_research_agent()`:
- Model: `Groq(id="llama-3.3-70b-versatile")`
- Tools: `DuckDuckGoTools`, `Newspaper4kTools`
- Guidance: Description, multi-phase instructions (Research → Analysis → Writing → Quality)
- Output: Markdown sections including sources with `https://` links

## Notes & Limitations
- If `GROQ_API_KEY` is missing, `/generate` returns an error and the app logs a warning at startup.
- The `src/text_summarization` package currently holds placeholders for future expansion and is not required for the core app flow.
- Long queries and extensive research may take 30–60 seconds or more.

## Development Tips
- Adjust the agent `description`, `instructions`, or `expected_output` in `app.py` to tailor report style.
- For production, disable `debug=True` and configure a proper WSGI server.
- Consider caching search results or articles if you expect repeated queries.

## License
Proprietary or as defined by the repository owner.
