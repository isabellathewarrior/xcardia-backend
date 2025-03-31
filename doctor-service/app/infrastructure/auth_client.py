import requests
from fastapi import HTTPException

AUTH_SERVICE_URL = "http://auth-service:8000/api"  # auth-service'in adresi

def register_doctor_in_auth_service(doctor_data):
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/register", json=doctor_data)
        if response.status_code == 201:
            return response.json()  # Doktor başarılı şekilde kaydedildi
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Auth service error: {str(e)}")

def login_doctor_in_auth_service(email: str, password: str):
    try:
        response = requests.post(f"{AUTH_SERVICE_URL}/login", data={"email": email, "password": password})
        if response.status_code == 200:
            return response.json()  # Login başarılı, token dönecek
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Auth service error: {str(e)}")
