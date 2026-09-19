from fastapi import FastAPI

from database.db import SessionLocal
from database.crud import get_metrics_since
from api.schemas import MetricResponse

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Linux Monitor API is running"}


@app.get("/metrics", response_model=list[MetricResponse])
def get_metrics():
    session = SessionLocal()

    try:
        return get_metrics_since(session, 30)
    finally:
        session.close()