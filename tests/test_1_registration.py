from locator import TestLocators
import re
import time

class TestRegistrations:
    def test_registration(self, driver, user, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.username_field).click()
        driver.find_element(*TestLocators.username_field).send_keys(user)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password)

        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).click()
        driver.find_element(*TestLocators.registration_email).send_keys("evgeniy_cheremisenko_3_016@test.ru")

        driver.find_element(*TestLocators.signin).click()
        time.sleep(3)

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()

    def test_name_not_empty(self, driver, user):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.username_field).click()
        driver.find_element(*TestLocators.username_field).send_keys(user)
        name = driver.find_element(*TestLocators.username_field).get_attribute("value")

        assert name != ""

        driver.quit()

    def test_email_format(self, driver, email):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).click()
        driver.find_element(*TestLocators.registration_email).send_keys(email)

        mail = driver.find_element(*TestLocators.registration_email).get_attribute("value")

        assert re.match(r'^\S+@\S+\.\S+$', mail)

    def test_min_password(self, driver, password):
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password)
        driver.find_element(*TestLocators.show_password).click()

        password = driver.find_element(*TestLocators.password_field).get_attribute("value")

        assert len(password) >= 6

    def test_password_error(self, driver, email, user):

        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(*TestLocators.username_field).click()
        driver.find_element(*TestLocators.username_field).send_keys(user)

        driver.find_element(*TestLocators.registration_email_area).click()
        driver.find_element(*TestLocators.registration_email).click()
        driver.find_element(*TestLocators.registration_email).send_keys(email)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys("111")

        driver.find_element(*TestLocators.signin).click()

        assert driver.find_element(*TestLocators.error)

        driver.quit()