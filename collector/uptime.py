import psutil
import time

def get_uptime():
    boot_time = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_time
    days = int(uptime_seconds // (24 * 3600))
    hours = int((uptime_seconds % (24 * 3600)) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return {
    "days": days,
    "hours": hours,
    "minutes": minutes,
    "uptime_seconds": uptime_seconds
    }
