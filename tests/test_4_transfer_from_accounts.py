from locator import TestLocators
import data
class TestTransfer:
    def test_transfer_from_construct(self, driver):

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.constructor_button).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_transfer_from_logo(self, driver):

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.email_field).send_keys(data.email_pretty)
        driver.find_element(*TestLocators.password_field).send_keys(data.password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.logo).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
