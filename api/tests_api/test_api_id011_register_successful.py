import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id011")
@allure.title("id011 Проверка получения статус кода 200 при успешной регистрации пользователя")
@pytest.mark.api
def test_api_register_successful():
    # Проверка получения статус кода 200 при успешной регистрации пользователя
    ApiSteps().check_register_successful()
