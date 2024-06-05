import pytest

from locators import TestLocators


class TestConstructorTabs:

    def test_click_on_tabs(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site')

        element = driver.find_element(*TestLocators.SAUCE_TAB_CONSTRUCTOR)  # начинаем со второго раздела Соусы, тк первый выбран по умолчанию
        assert "tab_tab_type_current" not in element.get_attribute("class")  # убеждаемся, что раздел не выбран
        driver.find_element(*TestLocators.SAUCE_TAB_CONSTRUCTOR).click()  # нажимаем по названию раздела
        assert "tab_tab_type_current" in element.get_attribute("class")  # проверяем, что после клика раздел стал выбранным

        element = driver.find_element(*TestLocators.FILLING_TAB_CONSTRUCTOR)  # повторяем те же дейстрий с разделом Начинки
        driver.find_element(*TestLocators.FILLING_TAB_CONSTRUCTOR).click()
        assert "tab_tab_type_current" in element.get_attribute("class")

        element = driver.find_element(*TestLocators.BUNS_TAB_CONSTRUCTOR)  # возвращаемся к первому разделу Булки
        driver.find_element(*TestLocators.BUNS_TAB_CONSTRUCTOR).click()
        assert "tab_tab_type_current" in element.get_attribute("class")

