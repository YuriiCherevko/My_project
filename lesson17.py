import argparse
import time
import math
import datetime as date

AUTHENTICATE_LIST = {
    "ivan": "qwerty",
    "vasyl": "12345",
    "olga": "qwerty12345",
}

fail_enter = None


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


def check_time():
    if date.datetime.now() < fail_enter:
        wait_minute = fail_enter - date.datetime.now()
        wait_minute = int(math.ceil(wait_minute.seconds / 60))
        print(f'Вы заблокированы! Следующая попытка через {wait_minute} мин.')
        time.sleep(61)
        check_time()
    else:
        print("Время блокировки истекло")


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
            fail_enter = date.datetime.now() + date.timedelta(minutes=5)
            check_time()
            attempt = 3

        print(f"У вас осталось {attempt} попыток")
