from selenium.webdriver.common.by import By
class TestLocators:
    username_field = By.NAME, "name"  # Поле "имя пользователя"
    registration_email_area = By.CSS_SELECTOR, ".Auth_fieldset__1QzWN:nth-child(2) .input"  # область ввода емайла
    registration_email = By.CSS_SELECTOR, ".input_status_active > .input__textfield"  # строка ввода емайла
    email_field = By.NAME, "name"  # Поле "емайл"
    password_field = By.NAME, "Пароль"  # Поле "пароль"
    signin = By.XPATH, ".//button[contains(.,'Зарегистрироваться')]"  # Кнопка "Зарегистрироваться"
    cabinet_button = By.LINK_TEXT, "Личный Кабинет"  # Кнопка "Личный кабинет"
    constructor_button = By.CSS_SELECTOR, "li:nth-child(1) .AppHeader_header__linkText__3q_va"  # Кнопка "Конструктор"
    logo = By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 svg"  # Логотип
    exit_button = By.CSS_SELECTOR, ".Account_button__14Yp3"  # Кнопка "Выход" из ЛК
    enter_button = By.CSS_SELECTOR, ".button_button__33qZ0"  # Кнопка "Войти в личный кабинет"
    bread_button = By.XPATH, "//span[text()='Булки']/parent::*"   # вкладка "Булки"
    sous_button = By.XPATH, '//span[text()="Соусы"]/parent::*'  # вкладка "Соусы"
    content_button = By.XPATH, "//span[text()='Начинки']/parent::*"  # вкладка "Начинки"
    show_password = By.CSS_SELECTOR, ".input__icon path"  # иконка показать/скрыть пароль
    error = By.XPATH, ".//p[contains(.,'Некорректный пароль')]"  # ошибка "некорректный пароль".
    enter_in_reg_form = By.CSS_SELECTOR, ".Auth_link__1fOlj"  # кнопка Войти в форме регистрации
    enter_in_recover_form = By.LINK_TEXT, "Войти"  # кнопка Войти в форме восстановления
    recover_password_button = By.LINK_TEXT, "Восстановить пароль" # кнопка "восстановить пароль"
    reg_button = By.LINK_TEXT, 'Зарегистрироваться'  # кнопка Зарегистрироваться под формой в ЛК
    menu_profile = By.XPATH, '//*[contains(@class, "Account_list_")]'
    name_in_profile = By.XPATH, '//*[text()="Имя"]/following-sibling::input'  # Поле имени
    ingredients_bar = By.XPATH, '//*[contains(@class, "tab_tab") and contains(@class, "current")]/child::span'  # Выбранная вкладка конструктора

