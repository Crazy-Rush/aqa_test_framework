import allure
import pytest

from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id025")
@allure.title("id025 Сверка статус кода и тела запроса кнопки Delete")
def test_ui_delete_user(browser):
    # клик на кнопку Delete
    MainPage(browser).click_button("delete_users_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_delete(f"{users_path}/2")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_delete(f"{users_path}/2")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
