from locator import TestLocators
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.ui import WebDriverWait
import data

class TestLogout:
    def test_logout_of_account(self, driver):

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(data.password)

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(data.email)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        driver.implicitly_wait(3)
        driver.find_element(*TestLocators.exit_button).click()
        WebDriverWait(driver,5).until_not(ex_cond.url_contains("/account/profile"))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'