import pytest

from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_registration_success(self, driver, new_name, new_login, new_password):

        driver.get('https://stellarburgers.nomoreparties.site/register')  # стр регистрации

        driver.find_element(*TestLocators.NAME_FIELD).send_keys(new_name)  # заполняем все поля
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()  # нажимаем по кнопке регистрации
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        # должны попасть на страницу входа, если регистрация успешна

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(new_login)  # вводим зарегистрированные данные
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(new_password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        # если залогинились, то на главной странце должна быть кнопка Оформить заказ
        assert WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.ORDER_BUTTON_MAIN_PAGE))

    def test_invalid_password(self, driver, valid_name, valid_login, invalid_password):
        driver.get('https://stellarburgers.nomoreparties.site/register')  # стр регистрации

        driver.find_element(*TestLocators.NAME_FIELD).send_keys(valid_name)  # заполняем все поля
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(valid_login)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(invalid_password)  # слишком короткий пароль

        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()  # нажимаем по кнопке регистрации
        #  должно появиться сообщение об ошибке
        assert WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PASSWORD_ERROR_MESSAGE))