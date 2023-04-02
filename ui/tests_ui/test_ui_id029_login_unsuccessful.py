import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import login_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id029")
@allure.title("id029 Сверка статус кода и тела запроса кнопки login_unsuccessful")
def test_ui_login_unsuccessful(browser):
    # Клик на кнопку login_unsuccessful
    MainPage(browser).click_button("login_unsuccessful_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_post(f"{login_path}", DataClient.login_with_invalid_data())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_post(f"{login_path}", DataClient.login_with_invalid_data())
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
