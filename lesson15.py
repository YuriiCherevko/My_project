AUTHENTICATE_LIST = {
    "ivan": "qwerty",
    "vasyl": "12345",
    "olga": "qwerty12345",
}
count = (i for i in range(3, 0, -1))


def login(func) -> bool:
    def wrapper():
        print("Введите имя")
        user_name = str(input()).strip().lower()
        print("Введите пароль")
        password = str(input()).strip()
        func(user_name, password)
        return True

    return wrapper


def authenticate(func) -> bool:
    def wrapper(user_name: str, password: str):
        func(user_name, password)
        return True

    return wrapper


@login
@authenticate
def check_password(user_name: str, password: str) -> bool:
    attempt = next(count)

    if AUTHENTICATE_LIST.get(user_name) == password:
        print("Вы в системе!")
        return True

    if attempt > 1:
        print("Не правильное Имя или Пароль")
        print(f"У вас осталось {attempt - 1} попыток")
        check_password()
        return False

    print("Не правильное Имя или Пароль")
    print("Попытки истекли!")
    return False


if __name__ == "__main__":
    check_password()
