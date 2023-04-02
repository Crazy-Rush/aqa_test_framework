import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id012")
@allure.title("id012 Проверка получения статус кода 400 при ошибочной регистрации пользователя")
@pytest.mark.api
def test_api_register_unsuccessful():
    # Проверка получения статус кода 400 при ошибочной регистрации пользователя
    ApiSteps().check_register_unsuccessful()
