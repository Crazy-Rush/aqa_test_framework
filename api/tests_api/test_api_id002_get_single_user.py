import allure
import pytest

from api.api_data.test_data.data_for_id_002_single_user import valid_users
from api.api_steps.steps_api import ApiSteps


@allure.id("id002")
@allure.title("id002 Проверка получения статус кода 200 для одного пользователя")
@pytest.mark.api
@pytest.mark.parametrize("expected_user", valid_users)
def test_get_single_user(expected_user):
    # Проверка получения статус кода 200 для одного пользователя
    ApiSteps().check_single_user_status_code()
