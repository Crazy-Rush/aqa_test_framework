from typing import Any

from api.api_data.base_requests import BaseRequests
from api.api_data.data_url import base_url, users_path, unknown_path, register_path, login_path


class RequestsForSite:
    def __init__(self) -> None:
        self.request = BaseRequests()
        self.base_url = base_url

    def get_request_users_path(self, params: str = None) -> Any:
        return self.request.get(url=f"{self.base_url}{users_path}{params}")

    def get_resource_unknown_path(self, params: str = None) -> Any:
        return self.request.get(url=f"{self.base_url}{unknown_path}{params}")

    def create_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{users_path}", json=payload)

    def put_update_user(self, payload: dict, user: int = 2) -> Any:
        return self.request.put(url=f"{self.base_url}{users_path}/{user}", json=payload)

    def patch_update_user(self, payload: dict, user: int = 2) -> Any:
        return self.request.patch(url=f"{self.base_url}{users_path}/{user}", json=payload)

    def delete_user(self, user: int = 2) -> Any:
        return self.request.delete(url=f"{self.base_url}{users_path}/{user}")

    def register_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{register_path}", json=payload)

    def login_user(self, payload: dict) -> Any:
        return self.request.post(url=f"{self.base_url}{login_path}", json=payload)

