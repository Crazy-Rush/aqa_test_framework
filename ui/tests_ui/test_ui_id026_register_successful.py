import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import register_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id026")
@allure.title("id026 Сверка статус кода и тела запроса кнопки register_successful")
def test_ui_register_successful(browser):
    # клик на кнопку register_successful
    MainPage(browser).click_button("register_successful_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_post(f"{register_path}", DataClient.register_successful_eve())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_post(f"{register_path}", DataClient.register_successful_eve())
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
