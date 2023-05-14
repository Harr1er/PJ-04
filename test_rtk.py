from selenium.webdriver.common.by import By
from config import *
import time


def test_auth_phone_positive(web_browser):
    # авторизация по номеру телефона
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # клик на кнопку "телефон"
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина(номер)
    field_phone = web_browser.find_element(By.ID, 'username')
    field_phone.send_keys(valid_phone)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://lk.rt.ru/'


def test_auth_phone_negative(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация без указания номера телефона
    web_browser.get(url_auth)
    # клик на кнопку "телефон"
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина(пустой номер)
    field_phone = web_browser.find_element(By.ID, 'username')
    field_phone.send_keys(empty_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Введите номер телефона"
    assert web_browser.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div > div:nth-of-type(2) > span'). \
               text == 'Введите номер телефона'


def test_auth_phone_short_number(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация с коротким номером
    web_browser.get(url_auth)
    # клик на кнопку 'телефон'
    btn_phone = web_browser.find_element(By.ID, 't-btn-tab-phone')
    btn_phone.click()
    # ввод логина
    field_phone = web_browser.find_element(By.ID, 'username')
    field_phone.send_keys(short_number)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Введите номер телефона"
    assert web_browser.find_element(By.XPATH, '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span'). \
               text == 'Неверный формат телефона'


def test_auth_mail(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по mail
    web_browser.get(url_auth)
    # клик на кнопку "email"
    btn_mail = web_browser.find_element(By.ID, 't-btn-tab-mail')
    btn_mail.click()
    # ввод логина(email)
    field_mail = web_browser.find_element(By.ID, 'username')
    field_mail.send_keys(valid_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://lk.rt.ru/'


def test_auth_mail_negative(web_browser):
    web_browser.implicitly_wait(2)
    # авторизация c пустым mail
    web_browser.get(url_auth)
    # клик на кнопку "email"
    btn_mail = web_browser.find_element(By.ID, 't-btn-tab-mail')
    btn_mail.click()
    # ввод логина(email)
    field_mail = web_browser.find_element(By.ID, 'username')
    field_mail.send_keys(empty_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Введите адрес, указанный при регистрации"
    assert web_browser.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > div > form > div >'
                                                     ' div:nth-of-type(2) > span').text == 'Введите адрес, указанный ' \
                                                                                           'при регистрации'


def test_auth_login_positive(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по логину
    web_browser.get(url_auth)
    # клик на кнопку "логин"
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_login = web_browser.find_element(By.ID, 'username')
    field_login.send_keys(valid_login)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://start.rt.ru/'


def test_auth_login_negative(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по логину c пустым паролем
    web_browser.get(url_auth)
    # клик на кнопку "логин"
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_mail = web_browser.find_element(By.ID, 'username')
    field_mail.send_keys(valid_login)
    # ввод пустого пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(empty_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Неверный логин или пароль"
    assert web_browser.find_element(By.CLASS_NAME, 'card-container__error login-form-container__error--bold').text == \
           'Неверный логин или пароль'


def test_auth_login_invalid_pass(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по логину c некорректным паролем
    web_browser.get(url_auth)
    # клик на кнопку "логин"
    btn_login = web_browser.find_element(By.ID, 't-btn-tab-login')
    btn_login.click()
    # ввод логина
    field_mail = web_browser.find_element(By.ID, 'username')
    field_mail.send_keys(valid_login)
    # ввод  пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(invalid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Неверный логин или пароль"
    assert web_browser.find_element(By.CSS_SELECTOR, 'section#page-right > div > div > p').text == \
           'Неверный логин или пароль'


def test_auth_account_positive(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по лицевому счету
    web_browser.get(url_auth)
    # клик на кнопку "лицевой счет"
    btn_account = web_browser.find_element(By.ID, 't-btn-tab-ls')
    btn_account.click()
    # ввод лицевого счета
    field_lc = web_browser.find_element(By.ID, 'username')
    field_lc.send_keys(valid_account)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # клик на кнопку "личный кабинет"
    btn_lk = web_browser.find_element(By.ID, 'lk-btn')
    btn_lk.click()
    # проверка входа в личный кабинет
    assert web_browser.current_url == 'https://start.rt.ru/?tab=main' or 'https://start.rt.ru/'


def test_auth_account_negative(web_browser):
    web_browser.implicitly_wait(3)
    # авторизация по лицевому счету c некорректным лицевым счетом
    web_browser.get(url_auth)
    # клик на кнопку "лицевой счет"
    btn_account = web_browser.find_element(By.ID, 't-btn-tab-ls')
    btn_account.click()
    # ввод некорректного лицевого счета
    field_lc = web_browser.find_element(By.ID, 'username')
    field_lc.send_keys(invalid_account)
    # ввод пустого пароля
    field_pass = web_browser.find_element(By.ID, 'password')
    field_pass.send_keys(valid_pass)
    # клик на кнопку "войти"
    btn_auth = web_browser.find_element(By.ID, 'kc-login')
    btn_auth.click()
    # проверка вывода сообщения "Неверный логин или пароль"
    assert web_browser.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/p[1]').text == \
           'Неверный логин или пароль'


def test_get_code(selenium):
    # получение временного кода на телефон и открытия формы ввода кода
    form = CodeForm(selenium)
    # ввод телефона
    form.address.send_keys(valid_phone)
    form.get_click()
    rt_code = form.driver.find_element(By.ID, 'rt-code-0')
    assert rt_code


def test_forgot_pass_phone(selenium):
    # восстановление пароля по номеру телефона
    form = AuthForm(selenium)
    # клик по надписи "Забыл пароль"
    form.forgot.click()
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    user = form.driver.find_element(By.ID, 'username')
    user.send_keys(valid_phone)
    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(25)
    assert reset_pass.text == 'Восстановление пароля'


def test_forgot_pass_email(selenium):
    # восстановление пароля по электронной почте
    form = AuthForm(selenium)
    # клик по надписи "Забыл пароль"
    form.forgot.click()
    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    user = form.driver.find_element(By.ID, 'username')
    user.send_keys(valid_email)
    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(25)
    assert reset_pass.text == 'Восстановление пароля'

def test_reg_positive(web_browser):
    # регистрация по email
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    time.sleep(1)
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    time.sleep(1)
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    time.sleep(1)
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    time.sleep(1)
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    time.sleep(1)
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    time.sleep(1)
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    time.sleep(2)
    # проверка входа в личный кабинет
    assert web_browser.find_element(By.XPATH, '// *[ @ id = "page-right"] / div[1] / div[1] / h1[1]').text == \
           'Подтверждение email'


def test_reg_short_name(web_browser):
    # регистрация - короткое имя
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод короткого имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(short_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_long_name(web_browser):
    # регистрация - длинное имя
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод короткого имени
    field_name = web_browser.find_element(By.NAME, 'firstName')
    field_name.send_keys(long_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[1]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_latin_lastname(web_browser):
    # регистрация фамилия на латинице
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    time.sleep(1)
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии на латинице
    time.sleep(1)
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(latin_lastname)
    # ввод почты
    time.sleep(1)
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    time.sleep(1)
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    time.sleep(1)
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    time.sleep(1)
    btn_reg = web_browser.find_element(By.NAME, 'register')
    btn_reg.click()
    time.sleep(1)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div[2]/span').text == \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_reg_short_pass(web_browser):
    # регистрация короткий пароль
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(short_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(short_pass)
    # сообщение о требуемом формате пароля
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Длина пароля должна быть не менее 8 символов'


def test_reg_lower_case_pass(web_browser):
    # пароль без заглавных букв
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(lower_case_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(lower_case_pass)
    # сообщение о требуемом формате пароля
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Пароль должен содержать хотя бы одну заглавную букву'


def test_reg_diff_pass(web_browser):
    # несовпадение паролей
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_reg_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    # сообщение о разных паролях
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[2]/span').text == \
           'Пароли не совпадают'


def test_reg_unique_mail(web_browser):
    # регистрация с неуникальным email
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод неуникальной почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_reg_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_reg_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    # сообщение о существовании учетной записи
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[1]/div/div/h2').text == \
           'Учётная запись уже существует'


def test_reg_long_phone(web_browser):
    # регистрация - длинный номер телефона
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод номера телефона
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(long_number)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(valid_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(valid_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    time.sleep(2)
    # сообщение о требуемом формате данных
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[3]/span').text == \
           'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


def test_reg_rus_pass(web_browser):
    # пароль на кириллице
    web_browser.implicitly_wait(3)
    web_browser.get(url_auth)
    # переход на страницу регистрации
    btn_reg = web_browser.find_element(By.XPATH, '//*[@id="kc-register"]')
    btn_reg.click()
    # ввод имени
    field_name = web_browser.find_element(By.NAME, "firstName")
    field_name.send_keys(valid_name)
    # ввод фамилии
    field_lastname = web_browser.find_element(By.NAME, "lastName")
    field_lastname.send_keys(valid_lastname)
    # ввод почты
    field_lastname = web_browser.find_element(By.ID, "address")
    field_lastname.send_keys(valid_reg_mail)
    # ввод пароля
    field_pass = web_browser.find_element(By.ID, "password")
    field_pass.send_keys(russian_pass)
    # подтверждение пароля
    field_pass_confirm = web_browser.find_element(By.ID, "password-confirm")
    field_pass_confirm.send_keys(russian_pass)
    # клик на кнопку "зарегистрироваться"
    btn_reg = web_browser.find_element(By.NAME, "register")
    btn_reg.click()
    # сообщение о разных паролях
    assert web_browser.find_element(By.XPATH,
                                    '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text == \
           'Пароль должен содержать только латинские буквы'