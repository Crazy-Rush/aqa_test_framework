import requests
from requests import Response


class BaseRequests:

    def get(self, url: str, params: dict = None) -> Response:
        return requests.request("GET", url=url, params=params)

    def patch(self, url: str, json: dict = None) -> Response:
        return requests.request("PATCH", url=url, json=json)

    def post(self, url: str, json: dict = None) -> Response:
        return requests.request("POST", url=url, json=json)

    def put(self, url: str, json: dict = None) -> Response:
        return requests.request("PUT", url=url, json=json)

    def delete(self, url: str) -> Response:
        return requests.request("DELETE", url=url)

