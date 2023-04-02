import allure
import pytest

from api.api_data.data_url import unknown_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id019")
@allure.title("id019 Сверка статус кода и тела запроса кнопки list_resource")
def test_ui_get_list_resource(browser):
    # Клик на кнопку list_resource
    MainPage(browser).click_button("list_resource_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{unknown_path}")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{unknown_path}")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
