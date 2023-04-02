class DataClient:

    @staticmethod
    def create_morpheus() -> dict:
        return {
            "name": "morpheus",
            "job": "leader"
        }

    @staticmethod
    def update_morpheus() -> dict:
        return {
            "name": "morpheus",
            "job": "zion resident"
        }

    @staticmethod
    def register_successful_eve() -> dict:
        return {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

    @staticmethod
    def register_with_invalid_data() -> dict:
        return {
            "email": "sydney@fife"
        }

    @staticmethod
    def login_successful_eve() -> dict:
        return {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

    @staticmethod
    def login_with_invalid_data() -> dict:
        return {
            "email": "peter@klaven"
        }