from locator import TestLocators
import data
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait

class TestEnterButtons:
    def test_enter_button(self, driver):
        driver.find_element(*TestLocators.enter_button).click()
        WebDriverWait(driver, 5).until(ex_cond.url_contains("/login"))

        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)

        WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.enter_button))
        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        WebDriverWait(driver, 5).until(ex_cond.url_contains("/profile"))

        assert "тестер" == driver.find_element(*TestLocators.name_in_profile).get_attribute("value")

    def test_enter_lk(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        WebDriverWait(driver, 5).until(ex_cond.url_contains("/profile"))

        assert "тестер" == driver.find_element(*TestLocators.name_in_profile).get_attribute("value")

    def test_enter_in_reg_form(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()
        driver.find_element(*TestLocators.enter_in_reg_form).click()
        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)
        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        WebDriverWait(driver, 5).until(ex_cond.url_contains("/profile"))

        assert "тестер" == driver.find_element(*TestLocators.name_in_profile).get_attribute("value")

    def test_enter_recover(self, driver):
        driver.find_element(*TestLocators.enter_button).click()
        driver.find_element(*TestLocators.recover_password_button).click()

        driver.find_element(*TestLocators.enter_in_recover_form).click()

        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)

        WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.enter_button))
        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        WebDriverWait(driver, 5).until(ex_cond.url_contains("/profile"))

        assert "тестер" == driver.find_element(*TestLocators.name_in_profile).get_attribute("value")