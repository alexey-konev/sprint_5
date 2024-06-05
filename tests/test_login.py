import pytest

from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_login_page_from_main_page(self, driver, new_login, new_password, new_name):

        driver.get('https://stellarburgers.nomoreparties.site/register')  # стр регистрации, создаем нового пользователя

        driver.find_element(*TestLocators.NAME_FIELD).send_keys(new_name)  # заполняем все поля
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()  # нажимаем по кнопке регистрации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        # после успешной регистрации попадаем на страницу логина

        driver.get('https://stellarburgers.nomoreparties.site')  # переходим на главную стр
        driver.find_element(*TestLocators.LOGIN_BUTTON_MAIN_PAGE).click()  # нажимаем по кнопке Войти в аккаунт
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))
        # ждем, что на странице логина загрузилась кнопка Войти
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        # если залогинились, то на главной странце должна быть кнопка Оформить заказ
        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))

    def test_login_from_personal_acc(self, driver, new_login, new_password):

        driver.get('https://stellarburgers.nomoreparties.site')  # главная стр

        driver.find_element(*TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE).click()  # нажимаем по кнопке Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа

        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))

    def test_login_from_registration_page(self, driver, new_login, new_password):

        driver.get('https://stellarburgers.nomoreparties.site/register')  # стр регистрации

        driver.find_element(*TestLocators.LOGIN_BUTTON_REGISTRATION_PAGE).click()  # нажимаем по кнопке Войти на стр регистрации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа

        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))

    def test_login_from_recovery_page(self, driver, new_login, new_password):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')  # стр восстановления пароля

        driver.find_element(*TestLocators.LOGIN_BUTTON_RECOVERY_PAGE).click()  # нажимаем по кнопке Войти на стр восс. пароля
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа

        assert WebDriverWait(driver, 6).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))
