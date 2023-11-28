from locator import TestLocators
class TestTransfer:
    def test_transfer_from_construct(self, driver, email_pretty, password_pretty):

        driver.get("https://stellarburgers.nomoreparties.site/login")


        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.constructor_button).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_transfer_from_logo(self, driver, email_pretty, password_pretty):

        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.logo).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()