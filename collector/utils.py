def bytes_to_gb(bytes_value):
    return round(bytes_value / (1024 ** 3), 2)

def print_section(title):
    print(title)
    print("-" * 20)