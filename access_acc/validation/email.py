import re


def valid_email(value):

    check_match = re.search(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", value)

    if not check_match:
        return False

    return True
