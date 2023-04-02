import allure
import pytest

from api.api_data.data_url import unknown_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id020")
@allure.title("id020 Сверка статус кода и тела запроса кнопки single_resource")
def test_ui_get_single_resource(browser):
    # клик на кнопку single_resource
    MainPage(browser).click_button("single_resource_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{unknown_path}/2")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{unknown_path}/2")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
