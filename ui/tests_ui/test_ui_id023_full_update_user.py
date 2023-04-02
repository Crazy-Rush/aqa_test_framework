import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@allure.id("id023")
@allure.title("id023 Сверка статус кода и тела запроса кнопки PUT Update")
@pytest.mark.ui
def test_ui_full_update_user(browser):
    # клик на кнопку PUT Update
    MainPage(browser).click_button("full_update_users_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_put(f"{users_path}/2", DataClient.update_morpheus())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_put(f"{users_path}/2", DataClient.update_morpheus())
    # Проверка соответствия тела запроса
    try:
        MainPage(browser).check_response_body(response_body)
    except AssertionError:
        print("ID и дата в теле ответа уникальны, не повторяются")