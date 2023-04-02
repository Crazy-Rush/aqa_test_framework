import allure
import pytest

from api.api_data.test_data.data_for_id_003_singe_user_not_found import users
from api.api_steps.steps_api import ApiSteps


@allure.id("id003")
@allure.title("id003 Проверка получения статус кода 404 для несуществующего пользователя")
@pytest.mark.api
@pytest.mark.parametrize("expect_user", users)
def test_api_get_single_user_not_found(expect_user):
    # Проверка получения статус кода 404 для несуществующего пользователя
    ApiSteps().check_single_user_not_found_status_code(user=23)
