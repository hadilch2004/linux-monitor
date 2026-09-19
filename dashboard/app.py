import streamlit as st

from database.db import SessionLocal
from database.crud import get_metrics_since
from database.crud import get_latest_metric


st.title("Linux Monitor")

session = SessionLocal()

try:
    metrics = get_metrics_since(session, 30)
    latest_metric = get_latest_metric(session)
finally:
    session.close()

data = {
    "timestamp": [metric.timestamp for metric in metrics],
    "cpu": [metric.cpu_percent for metric in metrics],
    "memory": [metric.memory_percent for metric in metrics]
}

col1, col2 = st.columns(2)

with col1:
    st.subheader("CPU Usage")
    st.line_chart(data, x="timestamp", y="cpu")

with col2:
    st.subheader("Memory Usage")
    st.line_chart(data, x="timestamp", y="memory")

st.metric(
    "Disk Usage",
    f"{latest_metric.disk_percent:.1f}%"
)