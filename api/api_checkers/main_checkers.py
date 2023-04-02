from typing import Any


class CommonChecker:
    default_message = "Некорректный статус код"

    @staticmethod
    def check_status_code_ok(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 200, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_201(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 201, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_204(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 204, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_400(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 400, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_status_code_404(r: Any, assertion_message: str = default_message) -> None:
        assert r.status_code == 404, f"{assertion_message}: {r.status_code}"

    @staticmethod
    def check_field_equals(
        field: Any, expected_value: Any, assertion_message: str = "Некорректное значение поля"
    ) -> None:
        assert field == expected_value, assertion_message
