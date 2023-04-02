import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id013")
@allure.title("id013 Проверка получения статус кода 200 при успешной авторизации пользователя")
@pytest.mark.api
def test_api_login_successful():
    # Проверка получения статус кода 200 при успешной авторизации пользователя
    ApiSteps().check_login_successful()
