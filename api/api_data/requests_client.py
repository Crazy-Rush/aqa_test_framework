from typing import Any

from api.api_data.base_requests import BaseRequests
from api.api_data.data_url import base_url, users_path, unknown_path, register_path, login_path


class RequestsForSite:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = base_url

    def get_list_users(self, page: int = 2) -> Any:
        return self.request.get(url=f"{self.base_url}{users_path}?page={page}")

    def get_single_user(self, user: int = 2) -> Any:
        return self.request.get(url=f"{self.base_url}{users_path}/{user}")

    def get_single_user_not_found(self, user: int = 23) -> Any:
        return self.request.get(url=f"{self.base_url}{users_path}/{user}")

    def get_list_resource(self) -> Any:
        return self.request.get(url=f"{self.base_url}{unknown_path}")

    def get_single_resource(self, user: int = 2) -> Any:
        return self.request.get(url=f"{self.base_url}{unknown_path}/{user}")

    def get_single_resource_not_found(self, user: int = 23) -> Any:
        return self.request.get(url=f"{self.base_url}{unknown_path}/{user}")

    def create_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{users_path}", json=payload)

    def full_update_user(self, payload: dict, user: int = 2) -> Any:
        return self.request.put(url=f"{self.base_url}{users_path}/{user}", json=payload)

    def update_user_info(self,  payload: dict, user: int = 2) -> Any:
        return self.request.patch(url=f"{self.base_url}{users_path}/{user}", json=payload)

    def delete_user(self, user: int = 2) -> Any:
        return self.request.delete(url=f"{self.base_url}{users_path}/{user}")

    def register_successful(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{register_path}", json=payload)

    def register_unsuccessful(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{register_path}", json=payload)

    def login_successful(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{login_path}", json=payload)

    def login_unsuccessful(self,payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{login_path}", json=payload)

    def delayed_response(self, delay: int = 3) -> Any:
        return self.request.get(url=f"{self.base_url}{users_path}?delay={delay}")
