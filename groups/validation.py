import re


def is_valid_group_name(name):
    pattern = r"^[A-Za-z][-A-Za-z0-9 ]*$"
    return re.match(pattern, name) is not None and len(name) <= 30
