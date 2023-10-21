import re

def is_valid_username(username):
    pattern = r"^[A-Z][a-zA-Z]*$"
    return re.match(pattern, username) is not None and len(username) <= 30
