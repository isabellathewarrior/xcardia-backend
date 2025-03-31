from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.infrastructure.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    specialty = Column(String)
    phone_number = Column(String)
    hospital = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
