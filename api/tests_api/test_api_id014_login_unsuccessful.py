import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id014")
@allure.title("id014 Проверка получения статус кода 400 при ошибочной авторизации пользователя")
@pytest.mark.api
def test_api_login_unsuccessful():
    # Проверка получения статус кода 400 при ошибочной авторизации пользователя
    ApiSteps().check_login_unsuccessful()
