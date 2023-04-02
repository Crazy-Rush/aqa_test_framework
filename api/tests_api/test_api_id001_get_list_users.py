import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id001")
@allure.title("id001 Проверка получения статус кода 200 для списка пользователей")
@pytest.mark.api
def test_get_list_users():
    # Проверка получения статус кода 200 для списка пользователей
    ApiSteps().check_list_users_status_code()
