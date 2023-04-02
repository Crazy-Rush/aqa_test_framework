import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import login_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id028")
@allure.title("id028 Сверка статус кода и тела запроса кнопки login_successful")
def test_ui_login_successful(browser):
    # Клик на кнопку login_successful
    MainPage(browser).click_button("login_successful_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_post(f"{login_path}", DataClient.login_successful_eve())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_post(f"{login_path}", DataClient.login_successful_eve())
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
