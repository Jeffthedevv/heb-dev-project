# H-E-B Developer Take-Home Project

### Overview
This small web application was built as part of the H-E-B developer interview process. It demonstrates backend and frontend engineering skills, including API design, database management, Docker-based containerization, and a simple React UI.

At this stage, the application is fully containerized and running successfully with both backend and frontend services.

---

### Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** React (Vite)
- **Database:** PostgreSQL (Dockerized)
- **Containerization:** Docker + Docker Compose

---

### Features Implemented 
#### Backend
- Dockerized PostgreSQL database with initialization script (`init.sql`)
- FastAPI backend with modular structure (`app/`)
- SQLAlchemy ORM models and Pydantic schemas
- Basic HTTP authentication (uploader/viewer roles)
- CSV file upload endpoint (bulk insert + validation)
- Paginated records API with optional name filtering
- CORS and structured error handling

#### Frontend
- React app initialized via Vite
- File upload form wired to `/upload` endpoint
- Paginated customer table with search filter
- Basic role integration for viewer/uploader
- Fully containerized frontend running on port `3000`

---

### Current Status
- Backend and database full functional
- Frontend connected and displaying data
- CSV uploads, filtering, and pagination all verified working

---

### How to Run (Full App)
```bash
# Build and start all services
docker compose up --build


### How to Run (Backend Only)
```bash
# build and run backend + db
Docker compose up --build
```

- Backend: [http://localhost:8000](http://localhost:8000)
- Frontend: [http://localhost:3000](http://localhost:3000)
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

#### Developed by Jeffery Diaz

--- 