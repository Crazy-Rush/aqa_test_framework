import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id005")
@allure.title("id005 Проверка получения статус кода 200 для одного предмета")
@pytest.mark.api
def test_api_get_single_resource():
    # Проверка получения статус кода 200 для одного предмета
    ApiSteps().check_single_resource_status_code(user=2)
