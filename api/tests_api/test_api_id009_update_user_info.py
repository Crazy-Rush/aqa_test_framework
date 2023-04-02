import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id009")
@allure.title("id009 Проверка получения статус кода 200 при изменении пользователя Patch запрос")
@pytest.mark.api
def test_api_update_user_info():
    # Проверка получения статус кода 200 при изменении пользователя
    ApiSteps().check_update_user()
