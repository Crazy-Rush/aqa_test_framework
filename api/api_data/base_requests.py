import requests
from requests import Response


class BaseRequests:

    @staticmethod
    def get(url: str, params: dict = None) -> Response:
        return requests.request("GET", url=url, params=params)

    @staticmethod
    def patch(url: str, json: dict = None) -> Response:
        return requests.request("PATCH", url=url, json=json)

    @staticmethod
    def post(url: str, json: dict = None) -> Response:
        return requests.request("POST", url=url, json=json)

    @staticmethod
    def put(url: str, json: dict = None) -> Response:
        return requests.request("PUT", url=url, json=json)

    @staticmethod
    def delete(url: str) -> Response:
        return requests.request("DELETE", url=url)

