
def valid_name(value):

    if len(value) < 4:
        return f"Name: {value} is too short, try another one please."

    if len(value) > 26:
        return f"Name: {value} is too long, try another one please."

    return False
