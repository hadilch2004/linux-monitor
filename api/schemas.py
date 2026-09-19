from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MetricResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    timestamp: datetime
    cpu_percent: float
    memory_percent: float
    disk_percent: float