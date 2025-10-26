from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
import csv, io
from ..database import get_db
from ..models import Customer
from ..auth import require_uploader

router = APIRouter(prefix="/upload", tags=["upload"]) 

@router.post("")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    role: str = Depends(require_uploader),
):
    # Validate file type early and exit if not CSV
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    # Read and parse CSV
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    reader = csv.DictReader(io.StringIO(text))

    # Collect rows (skip blanks) — simple, memory-friendly batch
    batch = []
    for row in reader:
        name = (row.get("name") or "").strip()
        email = (row.get("email") or None)
        if not name:
            continue
        batch.append({"name": name, "email": email})

    if not batch:
        return {"inserted": 0}

    # Insert in a single transaction
    try:
        db.bulk_insert_mappings(Customer, batch)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Insert failed: {e}")

    return {"inserted": len(batch)}
