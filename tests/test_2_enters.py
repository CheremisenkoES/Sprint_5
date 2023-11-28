from locator import TestLocators

class TestEnterButtons:
    def test_enter_button(self, driver, email_pretty, password_pretty):

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.enter_button).click()

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        assert '/stellarburgers.nomoreparties.site' in driver.current_url

        driver.quit()

    def test_enter_lk(self, driver, email_pretty, password_pretty):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.cabinet_button).click()

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        assert '/stellarburgers.nomoreparties.site' in driver.current_url

        driver.quit()

    def test_enter_in_reg_form(self, driver, email_pretty, password_pretty):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.enter_in_reg_form).click()

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        assert '/stellarburgers.nomoreparties.site' in driver.current_url

        driver.quit()

    def test_enter_recover(self, driver, email_pretty, password_pretty):
        # Проверь вход через кнопку в форме восстановления пароля.

        # Открыть сайт и зайти в ЛК
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(*TestLocators.enter_in_recover_form).click()

        driver.find_element(*TestLocators.email_field).click()
        driver.find_element(*TestLocators.email_field).send_keys(email_pretty)

        driver.find_element(*TestLocators.password_field).click()
        driver.find_element(*TestLocators.password_field).send_keys(password_pretty)

        driver.find_element(*TestLocators.enter_button).click()

        # Проверка страницы после успешного входа
        assert '/stellarburgers.nomoreparties.site' in driver.current_url

        driver.quit()