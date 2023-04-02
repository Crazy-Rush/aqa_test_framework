from typing import Any

import allure
import requests

from api.api_checkers.main_checkers import CommonChecker
from api.api_data.data_url import base_url
from ui.locators.main_page.main_page_locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class MainPage:
    def __init__(self, browser: webdriver.Chrome):
        self.locators = MainPageLocators
        self.browser = browser
        self.url = base_url

    @allure.step("Клик по кнопке")
    def click_button(self, locator: str) -> None:
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.locators.button_list_users_locator))
        list_button = self.browser.find_element(*getattr(self.locators, locator))
        list_button.click()

    @allure.step("получение статус кода запроса API GET запрос")
    def get_status_code_get(self, path: str) -> Any:
        status_code = requests.get(url=f"{self.url}{path}").status_code
        return status_code

    @allure.step("получение статус кода запроса API POST запрос")
    def get_status_code_post(self, path: str, json: dict = None) -> Any:
        status_code = requests.post(url=f"{self.url}{path}", json=json).status_code
        return status_code

    @allure.step("получение статус кода запроса API PUT запрос")
    def get_status_code_put(self, path: str, json: dict = None) -> Any:
        status_code = requests.put(url=f"{self.url}{path}", json=json).status_code
        return status_code

    @allure.step("получение статус кода запроса API PATCH запрос")
    def get_status_code_patch(self, path: str, json: dict = None) -> Any:
        status_code = requests.patch(url=f"{self.url}{path}", json=json).status_code
        return status_code

    @allure.step("получение статус кода запроса API DELETE запрос")
    def get_status_code_delete(self, path: str) -> Any:
        status_code = requests.delete(url=f"{self.url}{path}").status_code
        return status_code

    @allure.step("Сверка статус кода API запроса со статус кодом на ui странице")
    def check_status_code(self, status_code: Any) -> None:
        expected_status_code = self.browser.find_element(*self.locators.field_response_status_code_locator).text
        CommonChecker.check_field_equals(
            str(status_code), expected_status_code, assertion_message="Неверный статус код страницы"
        )

    @allure.step("получение тела запроса API GET запрос")
    def get_response_body_get(self, path: str) -> Any:
        body = requests.get(url=f"{self.url}{path}").json()
        return body

    @allure.step("получение тела запроса API POST запрос")
    def get_response_body_post(self, path: str, json: dict = None) -> Any:
        body = requests.post(url=f"{self.url}{path}", json=json).json()
        return body

    @allure.step("получение тела запроса API PUT запрос")
    def get_response_body_put(self, path: str, json: dict = None) -> Any:
        body = requests.put(url=f"{self.url}{path}", json=json).json()
        return body

    @allure.step("получение тела запроса API PATCH запрос")
    def get_response_body_patch(self, path: str, json: dict = None) -> Any:
        body = requests.patch(url=f"{self.url}{path}", json=json).json()
        return body

    @allure.step("получение тела запроса API DELETE запрос")
    def get_response_body_delete(self, path: str) -> Any:
        body = requests.delete(url=f"{self.url}{path}").text
        return body

    @allure.step("Сверка тела API запроса с телом на ui странице")
    def check_response_body(self, body: Any) -> None:
        expected_body = self.browser.find_element(
            *self.locators.field_response_body_locator
        ).text.replace('\n    ', '').replace('"', "'").replace(" ", "").replace("\n", "")
        CommonChecker.check_field_equals(
            str(body).replace(" ", ""), expected_body, assertion_message="Тело запроса не совпадает"
        )
