
def valid_password(value):

    if len(value) > 15:
        return "Your password is too long, try another one please."

    if len(value) < 6:
        return "Your password is too short, try another one please."

    return False
