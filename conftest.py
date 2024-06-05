import random
import pytest
import string
from selenium import webdriver


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1366,768')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")  # class, чтобы тесты не зависили друг от друга
def new_name():
    name_list = ['Саша', 'Маша', 'Паша', 'Каша']
    name = random.choice(name_list)
    return name


@pytest.fixture(scope="class")
def new_login():
    login = f"alexeykonev6{random.randint(1000, 9999)}@yandex.ru"
    return login


@pytest.fixture(scope="class")
def new_password():
    length = 6
    symbols = string.ascii_letters + string.digits  # все буквы в нижнем и верхнем регистрах + все цифры
    password = ''.join(random.choice(symbols) for i in range(length))
    return password

@pytest.fixture(scope="function")
def invalid_password():  # Для тестирования сообщения об ошибке при невалидном пароле
    length = 5  # слишком короткий пароль
    symbols = string.ascii_letters + string.digits  # все буквы в нижнем и верхнем регистрах + все цифры
    password = ''.join(random.choice(symbols) for i in range(length))
    return password


@pytest.fixture(scope="function")
def valid_name():  # Для тестирования сообщения об ошибке при невалидном пароле
    return "Длинноеимя"


@pytest.fixture(scope="function")
def valid_login():  # Для тестирования сообщения об ошибке при невалидном пароле
    return "alexeykonev6000@yandex.ru"
