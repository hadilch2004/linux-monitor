import psutil

def get_cpu_usage():
    """
    returns the current CPU usage percentage
    """
    return psutil.cpu_percent(interval=1) #wait one second to get a more accurate average
