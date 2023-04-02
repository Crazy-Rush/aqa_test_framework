import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id004")
@allure.title("id004 Проверка получения статус кода 200 для списка предметов")
@pytest.mark.api
def test_api_get_list_resource():
    # Проверка получения статус кода 200 для списка предметов
    ApiSteps().check_list_resource_status_code()
