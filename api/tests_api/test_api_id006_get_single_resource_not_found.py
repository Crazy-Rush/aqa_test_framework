import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id006")
@allure.title("id006 Проверка получения статус кода 404 для несуществующего предмета")
@pytest.mark.api
def test_api_get_single_resource_not_found():
    # Проверка получения статус кода 404 для несуществующего предмета
    ApiSteps().check_single_resource_not_found_status_code()
