from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime
from datetime import datetime

#Everything that inherits from me is a database model.
class Base(DeclarativeBase):
    pass
#this class isn't just a Python class—it's a table

class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id: Mapped[int] = mapped_column(primary_key=True)

    timestamp: Mapped[datetime] = mapped_column(default=datetime.now)

    cpu_percent: Mapped[float]

    memory_percent: Mapped[float]
    memory_used_gb: Mapped[float]

    disk_percent: Mapped[float]
    disk_used_gb: Mapped[float]

    network_sent_mb: Mapped[float]
    network_received_mb: Mapped[float]

    uptime_seconds: Mapped[int]