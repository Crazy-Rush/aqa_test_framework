import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import register_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id027")
@allure.title("id027 Сверка статус кода и тела запроса кнопки register_unsuccessful")
def test_ui_register_unsuccessful(browser):
    # клик на кнопку register_unsuccessful
    MainPage(browser).click_button("register_unsuccessful_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_post(f"{register_path}", DataClient.register_with_invalid_data())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_post(
        f"{register_path}", DataClient.register_with_invalid_data()
    )
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
