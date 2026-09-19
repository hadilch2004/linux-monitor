# Linux Server Monitoring Dashboard

A Python-based system monitoring project that collects OS metrics, stores them in PostgreSQL, exposes them through FastAPI, and visualizes them with Streamlit.

## Tech Stack

- Python
- psutil
- PostgreSQL
- SQLAlchemy
- FastAPI
- Uvicorn
- Streamlit
- Git / GitHub

## Current Features

- CPU monitoring
- Memory monitoring
- Disk monitoring
- Network usage collection
- System uptime
- Historical metric storage
- SQLAlchemy database queries
- Process CPU and memory monitoring
- FastAPI monitoring API
- Streamlit dashboard
- Historical CPU and memory graphs

## Architecture

```text
Operating System
       ↓
Python + psutil
       ↓
PostgreSQL
       ↓
SQLAlchemy
       ↓
FastAPI
       ↓
Streamlit


## Project structure
-------------------------
linux-monitor/
├── collector/
├── database/
├── api/
├── dashboard/
├── test_database.py
├── test_processes.py
├── requirements.txt
└── README.md


## Future Development
-------------------------
Pydantic API schemas
Flexible API time ranges
Process monitoring endpoints
Top CPU/memory processes
Network connections and listening ports
Network traffic monitoring
Logged-in user/session monitoring
Disk I/O monitoring
CPU frequency and temperature
Interrupt/IRQ monitoring
Threshold-based alerts
Alert history and active/resolved states
Browser notifications
More dashboard visualizations
Automated testing
Linux server deployment
Remote system monitoring

