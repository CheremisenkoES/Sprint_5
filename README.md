Sprint 5

conftest.py

> фикстура с запуском webdriver
> данные авторизации

locator.py

> тестовые локаторы сайта https://stellarburgers.nomoreparties.site 


test_1 Регистрация
> Успешная регистрация
> Поле «Имя» должно быть не пустым
> Поле Email введён email в формате логин@домен
> Минимальный пароль — шесть символов.
> Ошибка для некорректного пароля.

test_2 Вход
> вход по кнопке «Войти в аккаунт» на главной,
> вход через кнопку «Личный кабинет»,
> вход через кнопку в форме регистрации,
> вход через кнопку в форме восстановления пароля.

test_3 Переход на личный кабинет
> переход по клику на «Личный кабинет».

test_4 Переходы из личного кабинета
> переход из ЛК на конструктор
> переход из ЛК по логотипу

test_5 Выход
> выход по кнопке «Выйти» в личном кабинете.

test_6 Взаимодействие с конструктором бургеров
> работает переход к разделу «Булки»
> работает переход к разделу «Соусы»
> работает переход к разделу «Начинки»