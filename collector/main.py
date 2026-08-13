from collector.cpu import get_cpu_usage
from collector.memory import get_memory_usage
from collector.disk import get_disk_usage
from collector.network import get_network_usage
from collector.uptime import get_uptime
from collector.utils import print_section
import time

from database.models import SystemMetric
from database.db import SessionLocal
from database.crud import save_metric


print("System Resource Usage:")

while True:

    cpu = get_cpu_usage()
    print_section("CPU ")
    print(f"CPU Usage: {cpu}% \n ")



    memory = get_memory_usage()
    print_section("Memory ")
    print(f"Memory Usage: {memory['percent']}%")
    print(f"Memory Available: {memory['available_gb']} GB")
    print(f"Memory Used: {memory['used_gb']} GB")
    print(f"Memory Total: {memory['total_gb']} GB \n ")



    disk = get_disk_usage()

    print_section("Disk")

    print(f"Disk Usage: {disk['percent']}%")
    print(f"Disk Used: {disk['used_gb']} GB")
    print(f"Disk Free: {disk['free_gb']} GB")
    print(f"Disk Total: {disk['total_gb']} GB \n")



    network = get_network_usage()

    print_section("Network")

    print(f"Bytes received: {network['bytes_received']} MB")
    print(f"Bytes sent: {network['bytes_sent']} MB \n")



    uptime = get_uptime()

    print_section("Uptime")

    print(
        f"{uptime['days']} days, "
        f"{uptime['hours']} hours, "
        f"{uptime['minutes']} minutes\n"
    )




    #lets start talking to the database

    session = SessionLocal() 
    metric = SystemMetric(
        cpu_percent=cpu,

        memory_percent=memory["percent"],
        memory_used_gb=memory["used_gb"],

        disk_percent=disk["percent"],
        disk_used_gb=disk["used_gb"],

        network_sent_mb=network["bytes_sent"],
        network_received_mb=network["bytes_received"],

        uptime_seconds= uptime["uptime_seconds"],
    )

    try:
        save_metric(session, metric)
    finally:
        session.close()

    time.sleep(5)