FROM python:3.11
RUN mkdir /currency
WORKDIR /currency
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--bind=0.0.0.0:8000"]

# CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "unicorn.workers.UnicornWorker", "--bind=0.0.0.0:8000"]