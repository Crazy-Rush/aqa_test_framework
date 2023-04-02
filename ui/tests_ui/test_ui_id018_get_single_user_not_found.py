import allure
import pytest

from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id018")
@allure.title("id018 Сверка статус кода и тела запроса кнопки single_user_not_found")
def test_ui_get_single_user_not_found(browser):
    # Клик на кнопку single_user_not_found
    MainPage(browser).click_button("single_users_not_found_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_get(f"{users_path}/23")
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_get(f"{users_path}/23")
    # Проверка соответствия тела запроса
    MainPage(browser).check_response_body(response_body)
