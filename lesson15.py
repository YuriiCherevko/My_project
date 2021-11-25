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
    attempt = 3
    while True:
        print("Введите имя")
        user_name = str(input()).strip().lower()
        print("Введите пароль")
        password = str(input()).strip()
        res = login(user_name, password)
        if res:
            break
        attempt -= 1
        if attempt == 0:
            print("Не правильное Имя или Пароль")
            print("Попытки истекли!")
            break

        print(f"У вас осталось {attempt} попыток")
