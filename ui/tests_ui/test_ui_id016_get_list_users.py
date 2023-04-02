import allure
import pytest

from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id016")
@allure.title("id016 Сверка статус кода и тела запроса кнопки list_users")
def test_ui_get_list_users(browser):
    # Клик на кнопку list_users
    MainPage(browser).click_button("button_list_users_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{users_path}?page=2")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{users_path}?page=2")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
