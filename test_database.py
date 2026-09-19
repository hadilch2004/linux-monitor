from database.db import SessionLocal
from database.crud import get_cpu_avg

session = SessionLocal()

try:
    avg = get_cpu_avg(session)
    print(avg)

finally:
    session.close()