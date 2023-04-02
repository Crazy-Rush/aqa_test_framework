import allure
import pytest

from api.api_data.data_url import unknown_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id021")
@allure.title("id021 Сверка статус кода и тела запроса кнопки single_resource_not_found")
def test_ui_get_single_resource_not_found(browser):
    # клик на кнопку single_resource_not_found
    MainPage(browser).click_button("single_resource_not_found_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{unknown_path}/23")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{unknown_path}/23")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
