from validation.name import valid_name
from validation.email import valid_email
from validation.phone import valid_phone
from validation.password import valid_password
from sqlalchemy.orm import sessionmaker


def register_account(session: sessionmaker, schema):

    while True:

        user_name = input("Register/Enter name for you account: ")

        if session.query(schema).filter_by(name=user_name).first():
            print(
                f"Account with {user_name} already exists, please, try another name.")
            continue

        name_status = valid_name(user_name)

        if not name_status:
            break
        else:
            print(name_status)
            continue

    while True:

        user_email = input("Register/Enter email for your account: ")

        if session.query(schema).filter_by(email=user_email).first():
            print(
                f"Account with {user_email} already exists, please, try another email.")
            continue

        if valid_email(user_email):
            break
        else:
            print(
                f"{user_email} is of the wrong format, please, try something like this: <user_top1@gmail.com>.")
            continue

    while True:

        user_phone = input("Register/Enter phone number for your account: ")

        if session.query(schema).filter_by(phone=user_phone).first():
            print(
                f"Account with {user_phone} already exists, please, try another phone number.")
            continue

        if valid_phone(user_phone):
            break
        else:
            print(
                f"{user_phone} is of the wrong format, please, try these formats: (00)-000-0-000 | (00)-000-00-00.")
            continue

    while True:

        user_password = input("Register/Enter password for your account: ")

        password_status = valid_password(user_password)

        if not password_status:
            break
        else:
            print(password_status)
            continue

    new_user = schema(name=user_name, email=user_email,
                      phone=user_phone, password=user_password)
    session.add(new_user)
    session.commit()

    print("Account was successfully created!")
    return user_name
