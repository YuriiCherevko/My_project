import argparse

AUTHENTICATE_LIST = {
    "ivan": "qwerty",
    "vasyl": "12345",
    "olga": "qwerty12345",
}


def authenticate() -> bool:
    return True


def check_password(_user_name: str, _password: str) -> bool:
    if AUTHENTICATE_LIST.get(_user_name) == _password:
        print("Вы в системе!")
        return True
    return False


def dec_funk_login(funk):
    def wrapper(_user_name: str, _password: str):
        if not authenticate():
            return False
        if not check_password(_user_name, _password):
            return False
        return funk()

    return wrapper


@dec_funk_login
def login() -> bool:
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user_name", type=str, default=None, help="user_name")
    parser.add_argument("-p", "--password", type=str, default=None, help='password')
    args = parser.parse_args()

    attempt = 3
    while True:
        user_name = args.user_name
        password = args.password
        if user_name and password:
            if login(user_name, password):
                exit()

        if not user_name:
            print("Введите имя")
            user_name = str(input()).strip().lower()
        if not password:
            print("Введите пароль")
            password = str(input()).strip()
        if login(user_name, password):
            break
        attempt -= 1
        if attempt == 0:
            print("Не правильное Имя или Пароль")
            print("Попытки истекли!")
            break

        print(f"У вас осталось {attempt} попыток")
