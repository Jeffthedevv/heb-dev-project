from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Customer(Base):
  __tablename__ = "customers"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True)
  created_at = Column(DateTime, server_default=func.now())