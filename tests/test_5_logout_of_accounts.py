from locator import TestLocators
class TestLogout:
    def test_logout_of_account(self, driver, email, password):
        driver.get("https://stellarburgers.nomoreparties.site/login")

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password)

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email)

        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.cabinet_button).click()
        driver.implicitly_wait(10)

        driver.find_element(*TestLocators.exit_button)

        assert '/stellarburgers.nomoreparties.site' in driver.current_url
        driver.quit()
