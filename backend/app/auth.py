"""
Demo-grade auth utilities.

Provides two roles via HTTP Basic auth:
- uploader: can upload and view data
- viewer: can only view data

In production, replace with JWT or session auth backed by a user store.
"""
import os
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

UP_USER = os.getenv("DEMO_UPLOADER_USER", "uploader")
UP_PASS = os.getenv("DEMO_UPLOADER_PASS", "uploader123")
VW_USER = os.getenv("DEMO_VIEWER_USER", "viewer")
VW_PASS = os.getenv("DEMO_VIEWER_PASS", "viewer123")

ROLE_UPLOADER = "uploader"
ROLE_VIEWER = "viewer"

def _unauthorized():
    """Helper to standardize unauthorized responses."""
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )

async def require_role(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    """Return the caller's role or raise 401 if invalid."""
    if credentials.username == UP_USER and credentials.password == UP_PASS:
        return ROLE_UPLOADER
    if credentials.username == VW_USER and credentials.password == VW_PASS:
        return ROLE_VIEWER
    raise _unauthorized()

async def require_uploader(role: str = Depends(require_role)) -> str:
    """Ensure caller is an uploader; otherwise raise 403."""
    if role != ROLE_UPLOADER:
        raise HTTPException(status_code=403, detail="Uploader role required")
    return role