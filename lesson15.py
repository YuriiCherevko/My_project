AUTHENTICATE_LIST = {
    "ivan": "qwerty",
    "vasyl": "12345",
    "olga": "qwerty12345",
}


def check_password(func) -> bool:
    def wrapper(_user_name: str, _password: str):
        if AUTHENTICATE_LIST.get(_user_name) == _password:
            print("Вы в системе!")
            return func()
        return False

    return wrapper


def authenticate(func) -> bool:
    def wrapper():
        return True if func() else False

    return wrapper


@check_password
@authenticate
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
