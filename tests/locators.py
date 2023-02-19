logo = "//*[@id='root']/div/header/nav/div/a"  # Логотип

current_tab = "//*[contains(@class, 'tab_tab_type_current')]"  # Текущая вкладка

incorrect_pass_error = "//p[text()='Некорректный пароль']"  # Ошибка "Некорректный пароль"

main_page_title = "//h1[text() = 'Соберите бургер']"  # Текст на главной странице "Соберите бургер"

#Кнопки:

reg_button = "//*[@id='root']/div/main/div/form/button[text() = 'Зарегистрироваться']"  # Кнопка "Регистрация"

login_button = "//*[@id='root']/div/main/section[2]/div/button[text() = 'Войти в аккаунт']"  # Кнопка на главной странице "Войти в аккаунт"

sign_in_button = "//*[@id='root']/div/main/div/form/button[text() = 'Войти']"  # Кнопка "Войти" на странице входа

pa_button = "//a[@href = '/account']"  # Кнопка "Личный кабинет"

button_log_out = "//button[text()='Выход']"  # Кнопка "Выход"

button_reg_form = "//a[@href = '/login']"  # Кнопка "Войти" на странице регистрации

button_rec_password = "//a[text() = 'Восстановить пароль']"  # Кнопка "Восстановить пароль"

button_profile = "//a[text() = 'Профиль']"  # Кнопка перехода в профиль в личном кабинете

button_constructor = "//p[text() = 'Конструктор']/parent::a"  # Кнопка: "Конструктор"

button_for_placing_an_order = "//button[text() = 'Оформить заказ']"  # Кнопка "Оформить заказ"

#Поля для ввода:

name = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input[@name = 'name']"  # Поле ввода Имени

email_reg = "//label[text()='Email']/following-sibling::input"  # Поле для ввода E-Mail

password_reg = "//label[text()='Пароль']/following-sibling::input"  # Поле для ввода пароля

#Конструктор:

bread_section = "//span[text() = 'Булки']"  # Раздел "Булки" в конструкторе

sauces_section = "//span[text() = 'Соусы']"  # Раздел "Соусы" в конструкторе

topping_section = "//span[text() = 'Начинки']"  # Раздел "Начинки" в конструкторе