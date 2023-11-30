from locator import TestLocators
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait

class TestConstructor:
    def test_constructor_bread(self, driver):
        bread = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.bread_button))
        bread.find_element(*TestLocators.sous_button).click()
        bread.find_element(*TestLocators.bread_button).click()
        is_active = bread.find_element(*TestLocators.bread_button).get_attribute('class')
        assert 'current' in is_active

    def test_constructor_sous(self, driver):
        souse = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.sous_button))
        souse.click()
        WebDriverWait(driver, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.ingredients_bar, "Соусы"))
        is_active = souse.find_element(*TestLocators.sous_button).get_attribute('class')
        assert 'current' in is_active

    def test_constructor_content(self, driver):
        content = WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.content_button))
        content.click()
        WebDriverWait(driver, 10).until(ex_cond.text_to_be_present_in_element(TestLocators.ingredients_bar, "Начинки"))
        is_active = content.find_element(*TestLocators.content_button).get_attribute('class')
        assert 'current' in is_active
