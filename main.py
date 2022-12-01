from sqlalchemy import create_engine
from access_acc.accessing.register import register_account
from access_acc.accessing.login import login_into_acc
from session_folder.session_creation import create_session
from models import Account


def client_code(connection_string):

    engine = create_engine(connection_string)
    session = create_session(engine)

    print("Welcome to our service")

    while True:

        user_input = input("Choose an option: Register | Login: ")

        if user_input.lower() == "login":
            login = login_into_acc(session, Account)
            continue

        elif user_input.lower() == "register":
            register_account(session, Account)
            continue

        elif user_input.lower() in ['exit', 'close']:
            print("Goodbye")
            break

        else:
            print("Wrong input")
            continue


if __name__ == '__main__':
    client_code("sqlite:///database_prototype.db")
