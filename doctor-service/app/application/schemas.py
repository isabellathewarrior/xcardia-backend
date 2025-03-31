from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DoctorBase(BaseModel):
    name: str
    surname: str
    email: str
    specialty: str
    phone_number: str
    hospital: str

class DoctorCreate(DoctorBase):
    password: str

class DoctorOut(DoctorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
