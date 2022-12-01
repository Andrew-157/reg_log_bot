import re


def valid_phone(value):

    check_match = re.search(
        r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", value)

    if not check_match:
        return False

    return True
