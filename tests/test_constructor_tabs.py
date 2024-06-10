import pytest

from locators import TestLocators


class TestConstructorTabs:

    def test_click_on_tab_sauce(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        element = driver.find_element(*TestLocators.SAUCE_TAB_CONSTRUCTOR)  # второй разделл Соусы
        assert "tab_tab_type_current" not in element.get_attribute("class")  # убеждаемся, что раздел не выбран
        driver.find_element(*TestLocators.SAUCE_TAB_CONSTRUCTOR).click()  # нажимаем по названию раздела
        assert "tab_tab_type_current" in element.get_attribute("class")  # проверяем, что после клика раздел стал выбранным

    def test_click_on_tab_filling(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        element = driver.find_element(*TestLocators.FILLING_TAB_CONSTRUCTOR)  # повторяем те же дейстрий с разделом Начинки
        assert "tab_tab_type_current" not in element.get_attribute("class")
        driver.find_element(*TestLocators.FILLING_TAB_CONSTRUCTOR).click()
        assert "tab_tab_type_current" in element.get_attribute("class")

    def test_click_on_tab_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        driver.find_element(*TestLocators.SAUCE_TAB_CONSTRUCTOR).click()  # переходим на второй раздел Соусы, тк первый выбран по умолчанию

        element = driver.find_element(*TestLocators.BUNS_TAB_CONSTRUCTOR)
        assert "tab_tab_type_current" not in element.get_attribute("class")  # убеждаемся, что раздел не выбран
        driver.find_element(*TestLocators.BUNS_TAB_CONSTRUCTOR).click() # возвращаемся к первому разделу Булки
        assert "tab_tab_type_current" in element.get_attribute("class") # проверяем, что после клика раздел стал выбранным
