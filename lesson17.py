import argparse
import math
import datetime as date

AUTHENTICATE_LIST = {
    "ivan": {"password": "qwerty",
             "fail_enter": ''},
    "vasyl": {"password": "12345",
              "fail_enter": ''},
    "olga": {"password": "54321",
             "fail_enter": ''},
}


def fail_login(_user_name: str):
    user = AUTHENTICATE_LIST.get(_user_name, None)
    if not user:
        return False
    user['fail_enter'] = date.datetime.now() + date.timedelta(minutes=5)
    return False


def check_time(_user_name: str):
    user = AUTHENTICATE_LIST.get(_user_name, None)
    if not user:
        return False

    if user['fail_enter'] and date.datetime.now() < user['fail_enter']:
        wait_minute = user['fail_enter'] - date.datetime.now()
        wait_minute = int(math.ceil(wait_minute.seconds / 60))
        print(f'Вы заблокированы! Следующая попытка через {wait_minute} мин.')
        return False
    else:
        return True


def authenticate() -> bool:
    return True


def check_password(_user_name: str, _password: str) -> bool:
    user = AUTHENTICATE_LIST.get(_user_name, None)
    if user['password'] == _password:
        print("Вы в системе!")
        return True
    return False


def dec_funk_login(funk):
    def wrapper(_user_name: str, _password: str):
        if not check_time(_user_name):
            return False
        if not check_password(_user_name, _password):
            return False
        if not authenticate():
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
            fail_login(user_name)
            print("Не правильное Имя или Пароль")
            print("Вы заблокированы на 5 мин!")
            attempt = 3

        print(f"У вас осталось {attempt} попыток")
