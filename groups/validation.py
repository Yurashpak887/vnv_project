import re

def is_valid_group_name(name):
    pattern = r"^[A-Za-z][-A-Za-z0-9 ]*$"  # Дозволені букви (великі та малі), цифри, пробіли та "-"
    return re.match(pattern, name) is not None and len(name) <= 30
