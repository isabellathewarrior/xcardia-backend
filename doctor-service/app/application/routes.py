from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .schemas import DoctorCreate,DoctorOut, Token
from ..domain.services import create_doctor, authenticate_doctor
from ..infrastructure.database import get_db

router = APIRouter()

@router.post("/register", response_model=DoctorOut)
def register_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    try:
        db_doctor = create_doctor(db=db, doctor_data=doctor.dict())
        return db_doctor
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)

@router.post("/login", response_model=Token)
def login_doctor(email: str, password: str, db: Session = Depends(get_db)):
    token = authenticate_doctor(db=db, email=email, password=password)
    if token:
        return token
    raise HTTPException(status_code=401, detail="Invalid credentials")
