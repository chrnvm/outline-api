def get_format_value(bytes):
    factor = 1000
    for i in range(5):
        if bytes < factor:
            value = f"{bytes:.2f}" 
            return float(value)
        bytes /= factor


def get_unit(bytes, suffix="B"):
    factor = 1000
    for unit in ["", "k", "M", "G", "T"]:
        if bytes < factor:
            return f"{unit}{suffix}"
        bytes /= factor