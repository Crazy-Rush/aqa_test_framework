import allure
import pytest

from api.api_steps.steps_api import ApiSteps


@allure.id("id015")
@allure.title("id015 Проверка получения статус кода 200 при отсрочке запроса")
@pytest.mark.api
def test_api_delay_response():
    # Проверка получения статус кода 200 при отсрочке запроса
    ApiSteps().check_delayed_response()
