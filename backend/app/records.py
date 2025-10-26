from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import select
from .database import get_db
from .models import Customer
from .schemas import CustomerOut
from .auth import require_role 

router = APIRouter(prefix="/records", tags=["records"])

@router.get("", response_model=list[CustomerOut])
async def list_records(
  q: str | None = Query(None, description="Optional name filter"),
  limit: int = Query(20, ge=1, le=100),
  offset: int = Query(0, ge=0),
  db: Session = Depends(get_db),
  role: str = Depends(require_role),
):
  """
  Return paginated customers, optionally filtered by name.
  Notes:
    - Uses offset-based pagination for simplicity.
    - Adds ILIKE filter for case-insensitive search on name.
    - Sorted by newest first.
  """
  stmt = select(Customer)
  if q:
    stmt = stmt.filter(Customer.name.ilike(f"%{q}%"))
    stmt = stmt.order_by(Customer.created_at.desc()).limit(limit).offset(offset)
    rows = db.exec
    return rows