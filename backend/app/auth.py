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

# Returns role: str

async def require_role(credentials: HTTPBasicCredentials = Depends(security)):
  if credentials.username == UP_USER and credentials.password == UP_PASS:
    return ROLE_UPLOADER
  if credentials.username == VW_USER and credentials.password == VW_PASS:
    return ROLE_VIEWER
  raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
detail="Invalid credentials")

async def require_uploader(role: str = Depends(require_role)):
  if role != ROLE_UPLOADER:
    raise HTTPException(status_code=403, detail="Uploader role required")
  return role