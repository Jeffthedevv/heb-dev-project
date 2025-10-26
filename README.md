# H-E-B Developer Take-Home Project

### Overview
This is a small web application built as part of the H-E-B developer interview process. The goal is to demonstrate backend engineering skills including API design, database management, and containerization using Docker.

At this stage, the backend services are complete and running in Docker.

---

### Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL (Dockerized)
- **Containerization:** Docker + Docker Compose

---

### Features Implemented 
- Dockerized Postgres database with initialization script (`init.sql`)
- FastAPI backend with modular structure (`app/`)
- SQLAlchemy ORM models and Pydantic schemas
- Basic HTTP authentication with uploader/viewer roles
- CSV file upload endpoint (bulk insert with validation)
- Paginated record retrieval with filtering
- CORS, error handling, and minimal configuration

---

### To-Do (Frontend) 
- Set up React frontend using Vite
- Implement file upload form connected to backend
- Display paginated customer table with search filter
- Integrate basic role-based view (uploader vs viewer)
- Add frontend service to Docker Compose

---

### How to Run (Backend Only)
```bash
# build and run backend + db
Docker compose up --build
```

- Backend: [http://localhost:8000](http://localhost:8000)
- API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---