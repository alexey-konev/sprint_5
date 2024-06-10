import pytest
import data

from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogout:

    def test_logout_button_personal_acc(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/login')  # стр логина

        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(data.login)  # вводим данные тестового пользователя из data
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data.password)
        driver.find_element(*TestLocators.LOGIN_BUTTON_LOGIN_PAGE).click()  # кнопка входа
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE))
        # ждем, что загрузилась кнопка Личный кабинет

        driver.find_element(*TestLocators.PERSONAL_ACC_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACC_PROFILE))
        # ждем, что загрузилась вкладка Профиль в Личном кабинете
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

        driver.find_element(*TestLocators.LOGOUT_BUTTON_PERSONAL_ACC).click()  # нажимаем по кнопке выхода
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LOGIN_BUTTON_LOGIN_PAGE))

        # после выхода должны попасть на страницу логина
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
