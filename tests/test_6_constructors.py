from locator import TestLocators
class TestConstructor:
    def test_constructor_bread(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.content_button).click()
        driver.find_element(*TestLocators.bread_button).click()
        assert driver.find_element(*TestLocators.bread_button).text == 'Булки'
        driver.quit()

    def test_constructor_sous(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.sous_button).click()
        assert driver.find_element(*TestLocators.sous_button).text == 'Соусы'
        driver.quit()

    def test_constructor_content(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.content_button).click()
        assert driver.find_element(*TestLocators.content_button).text == 'Начинки'
        driver.quit()