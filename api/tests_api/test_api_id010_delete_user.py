import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id010")
@allure.title("id010 Проверка получения статус кода 200 при удалении пользователя")
@pytest.mark.api
def test_api_delete_user():
    # Проверка получения статус кода 200 при удалении пользователя
    ApiSteps().check_delete_user()
