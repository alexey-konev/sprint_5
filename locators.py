from selenium.webdriver.common.by import By


class TestLocators:
    NAME_FIELD = (By.XPATH, ".//*[text()='Имя']/following-sibling::input")  # поле ввода Имя
    EMAIL_FIELD = (By.XPATH, ".//*[text()='Email']/following-sibling::input")  # поле ввода Email
    PASSWORD_FIELD = (By.NAME, "Пароль")  # поле ввода Пароль
    REGISTRATION_BUTTON = (By.XPATH, ".//*[text() = 'Зарегистрироваться']")  # кнопка Зарегистрироваться
    PASSWORD_ERROR_MESSAGE = (By.XPATH, './/*[@class = "input__error text_type_main-default"]')  # сообщение об ошибке пароля

    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, './/*[contains(@class, "button_button_type_primary") and text()="Войти в аккаунт"]')  # кнопка Войти в аккаунт на главной стр
    PERSONAL_ACC_BUTTON_MAIN_PAGE = (By.XPATH, './/nav/a[contains(@class, "AppHeader_header__link")]')  # кнопка Личный кабинет на главной стр
    LOGIN_BUTTON_REGISTRATION_PAGE = (By.XPATH, './/*[contains(@class, "Auth_link")]')  # кнопка Войти на стр регистрации
    LOGIN_BUTTON_RECOVERY_PAGE = (By.XPATH, './/*[contains(@class, "Auth_link")]')  # кнопка Войти на стр восстановления пароля
    LOGIN_BUTTON_LOGIN_PAGE = (By.XPATH, './/*[contains(@class, "button_button_type_primary") and text()="Войти"]')  # кнопка Войти на стр входа
    ORDER_BUTTON_MAIN_PAGE = (By.XPATH, './/*[text()="Оформить заказ"]')  # кнопка Оформить заказ, если удалось залогиниться

    LOGO_HEADER = (By.XPATH, './/*[contains(@class, "AppHeader_header__logo")]')  # кликабельный логотип в хэдере
    CONSTRUCTOR_BUTTON_HEADER = (By.XPATH, './/*[text()="Конструктор"]/parent::*')  # кнопка Конструктор в хэдере
    PERSONAL_ACC_PROFILE = (By.XPATH, '.// *[contains(@class, "Account_link") and text()="Профиль"]')

    LOGOUT_BUTTON_PERSONAL_ACC = (By.XPATH, './/*[contains(@class, "Account_button")]')  # кнопка Выход в личном кабинете

    BUNS_TAB_CONSTRUCTOR = (By.XPATH, './/*[contains(@class, "tab_tab")]/*[text()="Булки"]/parent::*')  # переход на вкладку Булки в конструкторе
    SAUCE_TAB_CONSTRUCTOR = (By.XPATH, './/*[contains(@class, "tab_tab")]/*[text()="Соусы"]/parent::*')  # переход на вкладку Соусы в конструкторе
    FILLING_TAB_CONSTRUCTOR = (By.XPATH, './/*[contains(@class, "tab_tab")]/*[text()="Начинки"]/parent::*')  # переход на вкладку Начинки в конструкторе

