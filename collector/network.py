import psutil

def get_network_usage():
    network = psutil.net_io_counters()
    bytes_received = network.bytes_recv / (1024 * 1024)
    bytes_sent = network.bytes_sent / (1024 * 1024)


    return {
        "bytes_received" : round(bytes_received,2),
        "bytes_sent" : round(bytes_sent,2)   
    }