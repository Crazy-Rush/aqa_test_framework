from typing import Any

import allure

from api.api_checkers.main_checkers import CommonChecker
from api.api_data.api_data import DataClient
from api.api_data.requests_client import RequestsForSite


class ApiSteps:
    def __init__(self) -> None:
        self.request = RequestsForSite()
        self.data = DataClient()

    @allure.step("Проверка статус кода list_users")
    def check_list_users_status_code(self) -> Any:
        request = self.request.get_list_users()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить информацию о пользователях")
        return request

    @allure.step("Проверка статус кода single_user")
    def check_single_user_status_code(self, user) -> Any:
        request = self.request.get_single_user(user)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить информацию о пользователе")
        return request

    @allure.step("Проверка статус кода single_user_not_found")
    def check_single_user_not_found_status_code(self, user) -> Any:
        request = self.request.get_single_user(user)
        CommonChecker.check_status_code_404(
            request, assertion_message="Удалось найти пользователя с несуществующим номером"
        )

    @allure.step("Проверка статус кода list_resource")
    def check_list_resource_status_code(self) -> Any:
        request = self.request.get_list_resource()
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить список")

    @allure.step("Проверка статус кода single_resource")
    def check_single_resource_status_code(self) -> Any:
        request = self.request.get_single_resource(user=2)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось получить элемент списка")

    @allure.step("Проверка статус кода single_resource_not_found")
    def check_single_resource_not_found_status_code(self) -> Any:
        request = self.request.get_single_resource(user=23)
        CommonChecker.check_status_code_404(request, assertion_message="Удалось получить элемент списка")

    @allure.step("Проверка статус кода create_new_user")
    def check_create_new_user(self) -> Any:
        payload = self.data.create_morpheus()
        request = self.request.create_user(payload)
        CommonChecker.check_status_code_201(request, assertion_message="Не удалось создать пользователя")
        return request

    @allure.step("Проверка статус кода full_update_user")
    def check_full_update_user(self) -> Any:
        payload = self.data.update_morpheus()
        request = self.request.full_update_user(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось обновить пользователя")

    @allure.step("Проверка статус кода update_user")
    def check_update_user(self) -> Any:
        payload = self.data.update_morpheus()
        request = self.request.update_user_info(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось обновить пользователя")

    @allure.step("Проверка статус кода delete_user")
    def check_delete_user(self) -> Any:
        request = self.request.delete_user()
        CommonChecker.check_status_code_204(request, assertion_message="Не удалось удалить пользователя")

    @allure.step("Проверка статус кода register_successful")
    def check_register_successful(self) -> Any:
        payload = self.data.register_successful_eve()
        request = self.request.register_user(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось зарегистрировать пользователя")

    @allure.step("Проверка статус кода register_unsuccessful")
    def check_register_unsuccessful(self) -> Any:
        payload = self.data.register_with_invalid_data()
        request = self.request.register_user(payload)
        CommonChecker.check_status_code_400(
            request, assertion_message="Удалось зарегистрировать пользователя с неверными данными"
        )

    @allure.step("Проверка статус кода login_successful")
    def check_login_successful(self) -> Any:
        payload = self.data.login_successful_eve()
        request = self.request.login_user(payload)
        CommonChecker.check_status_code_ok(request, assertion_message="Не удалось авторизоваться")

    @allure.step("Проверка статус кода login_unsuccessful")
    def check_login_unsuccessful(self) -> Any:
        payload = self.data.login_with_invalid_data()
        request = self.request.login_user(payload)
        CommonChecker.check_status_code_400(request, assertion_message="Удалось авторизоваться с неверными данными")

    @allure.step("Проверка статус кода delayed_response")
    def check_delayed_response(self) -> Any:
        request = self.request.delayed_response()
        CommonChecker.check_status_code_ok(request, assertion_message="Не верно отправлен запрос")
