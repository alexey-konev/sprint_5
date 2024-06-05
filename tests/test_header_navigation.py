import pytest

from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestHeaderNavigation:

    def test_personal_acc_from_main_page(self, driver, new_login, new_password, new_name):
        driver.get('https://stellarburgers.nomoreparties.site/register')  # стр регистрации, создаем нового пользователя

        driver.find_element(*TestLocators.NAME_FIELD).send_keys(new_name)  # заполняем все поля
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()  # нажимаем по кнопке регистрации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        # после успешной регистрации попадаем на страницу логина

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE))
        # ждем, что загрузилась кнопка Личный кабинет

        driver.find_element(*TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_PROFILE))
        # ждем, что загрузилась вкладка Профиль в Личном кабинете
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_main_page_from_constructor_button(self, driver, new_login, new_password, new_name):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE))
        # ждем, что загрузилась кнопка Личный кабинет

        driver.find_element(*TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_PROFILE))
        # ждем, что загрузилась вкладка Профиль в Личном кабинете
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON_HEADER).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_main_page_from_logo(self, driver, new_login, new_password, new_name):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE))
        # ждем, что загрузилась кнопка Личный кабинет

        driver.find_element(*TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_PROFILE))
        # ждем, что загрузилась вкладка Профиль в Личном кабинете
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*TestLocators.LOGO_HEADER).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

