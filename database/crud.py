from sqlalchemy.orm import Session #it shouldnt know session local

from database.models import SystemMetric

def save_metric(session: Session, metric: SystemMetric):
    session.add(metric)
    session.commit()
    


