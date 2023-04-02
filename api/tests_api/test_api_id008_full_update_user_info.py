import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id008")
@allure.title("id008 Проверка получения статус кода 200 при изменении пользователя PUT запрос")
@pytest.mark.api
def test_api_full_update_user_info():
    # Проверка получения статус кода 200 при изменении пользователя
    ApiSteps().check_full_update_user()
