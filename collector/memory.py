import psutil
from collector.utils import bytes_to_gb
def get_memory_usage():
    """
    returns the current memory usage percentage,available memory, and total memory
    """
    memory = psutil.virtual_memory()

    #total_gb = memory.total / (1024 ** 3)
    #used_gb = memory.used / (1024 ** 3)
    #available_gb = memory.available / (1024 ** 3)
    #percent = memory.percent

    return {
       "total_gb": bytes_to_gb(memory.total),
       "used_gb":bytes_to_gb(memory.used),
        "available_gb": bytes_to_gb(memory.available),
        "percent": round(memory.percent,2),
        "total_bytes": memory.total
    }