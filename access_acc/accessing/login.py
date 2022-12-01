from sqlalchemy.orm import sessionmaker
from random import randint
from sqlalchemy.sql import select


def login_into_acc(session: sessionmaker, schema):

    login_status = ""
    password_attempts_counter = 0
    phone_attempts_counter = 0

    while True:

        user_name = input("Login/Enter account's name: ")

        if not session.query(schema).filter_by(name=user_name).first():
            print(
                f"Account with name: {user_name} doesn't exist, try again, please.")
            continue

        break

    stmt_for_email = select(schema.email).where(schema.name == user_name)

    mail = []

    for email in session.execute(stmt_for_email):
        mail.append(email)

    true_email = mail[0][0]

    while True:

        user_email = input("Login/Enter account's email: ")

        if user_email != true_email:
            print("Your account has another email, try again, please.")
            continue
        break

    stmt_for_password = select(schema.password).where(schema.name == user_name)

    psw = []

    for password in session.execute(stmt_for_password):
        psw.append(password)

    true_password = psw[0][0]

    while True:

        if password_attempts_counter > 3:
            print("Cannot login into account, wrong password")
            login_status = "Failed to login"
            return login_status

        user_password = input("Login/Enter account's password: ")

        if user_password != true_password:
            password_counter += 1
            print(
                f"Wrong password, {3-password_attempts_counter} attempts left")
            continue
        break

    stmt_for_phone = select(schema.phone).where(schema.name == user_name)

    phone_number = []

    for phone in session.execute(stmt_for_phone):
        phone_number.append(phone)

    true_phone = phone_number[0][0]

    while True:

        user_phone = input("Login/Enter phone for your account: ")

        if user_phone != true_phone:
            print("Your account has another phone number, try again, please.")
            continue

        while True:

            if phone_attempts_counter > 3:
                print("Cannot login into account, failed phone number authorization")
                login_status = "Login failed, failed authorization with phone number"

            code = randint(1000, 9999)
            print(code)

            user_code = input("Please, enter the code that we sent you: ")
            if user_code != code:
                phone_attempts_counter += 1
                print(
                    f"Wrong code, try again: {3-phone_attempts_counter} attempts left")
                continue

    return login_status
