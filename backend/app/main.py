from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import upload, records

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HEB Panel API")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(records.router)
