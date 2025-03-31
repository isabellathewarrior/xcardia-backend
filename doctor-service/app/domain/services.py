from sqlalchemy.orm import Session
from .models import Doctor
from .exceptions import DoctorAlreadyExistsError
from app.infrastructure.auth_client import register_doctor_in_auth_service, login_doctor_in_auth_service

def create_doctor(db: Session, doctor_data: dict):
    # Doktor daha önce kaydedilmiş mi kontrol et
    db_doctor = db.query(Doctor).filter(Doctor.email == doctor_data['email']).first()
    if db_doctor:
        raise DoctorAlreadyExistsError(f"Doctor with email {doctor_data['email']} already exists.")
    
    # Auth-service üzerinden doktor kaydını yap
    auth_response = register_doctor_in_auth_service(doctor_data)
    
    # Veritabanına doktoru kaydet
    db_doctor = Doctor(**doctor_data)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    
    return db_doctor

def authenticate_doctor(db: Session, email: str, password: str):
    # Auth-service üzerinden giriş yap
    token = login_doctor_in_auth_service(email, password)
    
    if token:
        return {"access_token": token["access_token"], "token_type": token["token_type"]}
    return None
