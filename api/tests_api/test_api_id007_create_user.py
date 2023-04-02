import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id007")
@allure.title("id007 Проверка получения статус кода 200 при создании пользователя")
@pytest.mark.api
def test_api_create_user():
    # Проверка получения статус кода 200 при создании пользователя
    ApiSteps().check_create_new_user()
