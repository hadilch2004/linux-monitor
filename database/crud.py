from sqlalchemy.orm import Session #it shouldnt know session local
from sqlalchemy import func
from database.models import SystemMetric
from datetime import datetime, timedelta

def save_metric(session: Session, metric: SystemMetric):
    session.add(metric)
    session.commit()

def get_latest_metric(session: Session):
    return (
        session.query(SystemMetric)
        .order_by(SystemMetric.timestamp.desc())
        .first()
    )
def get_recent_metrics(session: Session , limit : int =10):
    return(
        session.query(SystemMetric)
        .order_by(SystemMetric.timestamp.desc())
        .limit(limit)
        .all()
    )
def get_cpu_avg(session: Session):
    return (
        session.query(func.avg(SystemMetric.cpu_percent))
        .scalar()
    )
def get_max_cpu(session : Session):
    return(
        session.query(func.max(SystemMetric.cpu_percent))
        .scalar()
    )

def get_metrics_since(session: Session, minutes: int):
    cutoff = datetime.now() - timedelta(minutes=minutes)

    return (
        session.query(SystemMetric)
        .filter(SystemMetric.timestamp >= cutoff)
        .all()
    )