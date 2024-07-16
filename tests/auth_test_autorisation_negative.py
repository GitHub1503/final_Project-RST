import pytest
from pages.auth_page import AuthPage
from conftest import chrome_browser_instance

@pytest.fixture(scope="function")
def auth_page(chrome_browser_instance):
    return AuthPage(chrome_browser_instance)

def test_invalid_autorisation_by_email(auth_page):
    auth_page.btn_tab_email.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('error.spb@gmail.com')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('QWERTY12345qwerty')

    auth_page.btn_enter.click()

    sms = auth_page.err.get_text()
    assert sms == 'Неверный логин или пароль'

def test_invalid_autorisation_by_password(auth_page):
    auth_page.btn_tab_email.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('gavrilovdan.spb@gmail.com')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('asrg35eh')

    auth_page.btn_enter.click()

    sms = auth_page.err.get_text()
    assert sms == 'Неверный логин или пароль'

def test_invalid_autorisation_by_phone(auth_page):
    #auth_page.btn_tab_email.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('89999999999')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('QWERTY12345qwerty')

    auth_page.btn_enter.click()

    sms = auth_page.err.get_text()
    assert sms == 'Неверный логин или пароль'

def test_invalid_autorisation_by_login(auth_page):
    auth_page.btn_tab_login.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('wsrg-213423565')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('QWERTY12345qwerty')

    auth_page.btn_enter.click()

    sms = auth_page.err.get_text()
    assert sms == 'Неверный логин или пароль'

def test_invalid_autorisation_by_ls(auth_page):
    auth_page.btn_tab_ls.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('272528538635227')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('QWERTY12345qwerty')

    auth_page.btn_enter.click()

    sms = auth_page.err.get_text()
    assert sms == 'Неверный логин или пароль'