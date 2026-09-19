import psutil
import time


def get_processes():
    processes = []

    # Establish CPU baseline
    for process in psutil.process_iter():
        try:
            process.cpu_percent(None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    time.sleep(1)


    for process in psutil.process_iter():
        try:
            cpu = process.cpu_percent(None)
            memory = process.memory_percent()

            processes.append((process, cpu, memory))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return processes
# we found the processes and returned them appending eavh process to the list
