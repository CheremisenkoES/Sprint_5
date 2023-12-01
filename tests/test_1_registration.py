from locator import TestLocators
import re
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import data


class TestRegistrations:
    def test_registration(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()

        driver.find_element(*TestLocators.username_field).send_keys("evgeniy")
        driver.find_element(*TestLocators.password_field).send_keys("111111")
        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).send_keys("evgeniy_cheremisenko_3_020@test.ru")

        WebDriverWait(driver, 5).until(ex_cond.element_to_be_clickable(TestLocators.signin))
        driver.find_element(*TestLocators.signin).click()

        WebDriverWait(driver, 5).until_not(ex_cond.url_contains("/register"))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_name_not_empty(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()

        driver.find_element(*TestLocators.username_field).click()
        driver.find_element(*TestLocators.username_field).send_keys(data.user)
        name = driver.find_element(*TestLocators.username_field).get_attribute("value")

        assert name != ""


    def test_email_format(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()

        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).send_keys(data.email)

        mail = driver.find_element(*TestLocators.registration_email).get_attribute("value")

        assert re.match(r'^\S+@\S+\.\S+$', mail)

    def test_min_password(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(data.password)
        driver.find_element(*TestLocators.show_password).click()

        password = driver.find_element(*TestLocators.password_field).get_attribute("value")

        assert len(password) >= 6

    def test_password_error(self, driver):
        driver.find_element(*TestLocators.cabinet_button).click()
        driver.find_element(*TestLocators.reg_button).click()

        driver.find_element(*TestLocators.username_field).click()
        driver.find_element(*TestLocators.username_field).send_keys(data.user)

        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).send_keys(data.email)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys("111")

        driver.find_element(*TestLocators.signin).click()

        assert driver.find_element(*TestLocators.error)