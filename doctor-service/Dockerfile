# Python 3.12 tabanlı bir imaj kullanıyoruz.
FROM python:3.12-slim

# Çalışma dizinini belirliyoruz.
WORKDIR /app

# Gerekli Python paketlerinin listelendiği requirements.txt dosyasını imaja kopyalıyoruz.
COPY requirements.txt .

# Python bağımlılıklarını yüklüyoruz.
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını Docker imajına kopyalıyoruz.
COPY . .

# Uygulamanın çalışacağı portu belirliyoruz (FastAPI varsayılan olarak 8000'de çalışır).
EXPOSE 8000

# FastAPI uygulamasını başlatmak için Uvicorn kullanıyoruz.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
