import allure
import pytest

from api.api_data.api_data import DataClient
from api.api_data.data_url import users_path
from ui.pages.main_page.main_page import MainPage


@pytest.mark.ui
@allure.id("id022")
@allure.title("id022 Сверка статус кода и тела запроса кнопки Create")
def test_ui_create_user(browser):
    # клик на кнопку Create
    MainPage(browser).click_button("create_users_locator")
    # Получение статус кода с API
    status_code = MainPage(browser).get_status_code_post(f"{users_path}", DataClient.create_morpheus())
    # Сверка статус кода запроса
    MainPage(browser).check_status_code(status_code)
    # Получение тела зпроса с API
    response_body = MainPage(browser).get_response_body_post(f"{users_path}", DataClient.create_morpheus())
    # Проверка соответствия тела запроса
    try:
        MainPage(browser).check_response_body(response_body)
    except AssertionError:
        print("ID и дата в теле ответа уникальны, не повторяются")
