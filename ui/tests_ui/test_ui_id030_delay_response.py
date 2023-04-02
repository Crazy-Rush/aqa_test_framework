import allure
import pytest

from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id030")
@allure.title("id030 Сверка статус кода и тела запроса кнопки delay_response")
def test_ui_delay_response(browser):
    # Клик на кнопку delay_response
    MainPage(browser).click_button("delay_response_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{users_path}?delay=3")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{users_path}?delay=3")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
