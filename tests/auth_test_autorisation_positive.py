import pytest
from pages.auth_page import AuthPage
from conftest import chrome_browser_instance

@pytest.fixture(scope="function")
def auth_page(chrome_browser_instance):
    return AuthPage(chrome_browser_instance)

def test_valid_autorisation_by_email(auth_page):
    auth_page.btn_tab_email.click()
    auth_page.input_username.click()
    auth_page.input_username.send_keys('gavrilov1979@gmail.com')

    auth_page.input_password.click()
    auth_page.input_password.send_keys('1234_56789Qq')

    auth_page.btn_enter.click()

    name = auth_page.fio.get_text()
    assert name == 'Учетные данные'

def test_valid_autorisation_by_login(auth_page):
    auth_page.btn_tab_login.click()
    auth_page.input_username.click()

    auth_page.input_username.send_keys('rtkid_1721135410929')

    auth_page.input_password.click()

    auth_page.input_password.send_keys('1234_56789Qq')

    auth_page.btn_enter.click()

    name = auth_page.fio.get_text()

    assert name == 'Учетные данные'

