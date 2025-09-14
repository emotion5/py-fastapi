# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Application Architecture

This is a dual-server fullstack application for learning FastAPI:

- **Backend (main.py)**: FastAPI REST API server providing memo CRUD operations
- **Frontend (streamlit_app.py)**: Streamlit web interface that communicates with the FastAPI backend via httpx

The architecture follows a clear separation:
```
User Browser → Streamlit (port 8501) → FastAPI API (port 8000) → In-memory storage
```

Data flows through the Streamlit frontend which makes HTTP calls to the FastAPI backend. Users only interact with the Streamlit interface - they never directly access the FastAPI server.

## Key Components

**Backend (main.py)**:
- Uses in-memory storage (`memos_db` list) with auto-incrementing IDs
- Provides REST endpoints: GET /memos, POST /memos, DELETE /memos/{id}
- Simple Pydantic model: `Memo` with single `content` field
- Root endpoint provides API documentation links

**Frontend (streamlit_app.py)**:
- Uses httpx for API communication (not requests)
- Implements gray-scale minimal design with custom CSS
- Provides real-time UI updates with `st.rerun()`
- Includes connection checking to ensure backend is running

## Common Commands

**Development Setup**:
```bash
uv sync  # Install all dependencies including streamlit
```

**Running the Application** (requires 2 terminals):
```bash
# Terminal 1: Backend API server
uvicorn main:app --reload

# Terminal 2: Frontend web interface
streamlit run streamlit_app.py
```

**Access Points**:
- Main app: http://localhost:8501 (Streamlit frontend)
- API docs: http://localhost:8000/docs (FastAPI Swagger UI)
- API root: http://localhost:8000/ (API endpoint list)

## Development Notes

- Both servers must be running for full functionality
- The frontend automatically checks backend connectivity on startup
- Data is stored in memory only - restarting the backend clears all memos
- The project uses uv for dependency management (not pip)
- Korean language is used in the UI and API responses for learning purposes