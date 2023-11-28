from locator import TestLocators
class TestPersonalAccount:
    def test_click_on_personal_acc(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.cabinet_button).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
