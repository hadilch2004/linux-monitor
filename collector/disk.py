import psutil

def get_disk_usage():

    disk = psutil.disk_usage("/")

    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used  / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)
    percent = disk.percent  

    return {
        "total_gb":round(total_gb,2),
        "used_gb":round(used_gb,2),
        "free_gb":round(free_gb,2),
        "percent":round(percent,2)
    }

 

