from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.domain.models import Base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:projecT41@localhost/xcardia"  # PostgreSQL bağlantı URL'si

engine = create_engine(SQLALCHEMY_DATABASE_URL)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablosunun oluşturulması
def init_db():
    Base.metadata.create_all(bind=engine)
