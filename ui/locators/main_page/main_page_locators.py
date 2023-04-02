from selenium.webdriver.common.by import By


class MainPageLocators:
    button_list_users_locator = (By.XPATH, '//*[@data-id="users"]')
    single_users_locator = (By.XPATH, '//*[@data-id="users-single"]')
    single_users_not_found_locator = (By.XPATH, '//*[@data-id="users-single-not-found"]')
    list_resource_locator = (By.XPATH, '//*[@data-id="unknown"]')
    single_resource_locator = (By.XPATH, '//*[@data-id="unknown-single"]')
    single_resource_not_found_locator = (By.XPATH, '//*[@data-id="unknown-single-not-found"]')
    create_users_locator = (By.XPATH, '//*[@data-id="post"]')
    full_update_users_locator = (By.XPATH, '//*[@data-id="put"]')
    update_users_locator = (By.XPATH, '//*[@data-id="patch"]')
    delete_users_locator = (By.XPATH, '//*[@data-id="delete"]')
    register_successful_locator = (By.XPATH, '//*[@data-id="register-successful"]')
    register_unsuccessful_locator = (By.XPATH, '//*[@data-id="register-unsuccessful"]')
    login_successful_locator = (By.XPATH, '//*[@data-id="login-successful"]')
    login_unsuccessful_locator = (By.XPATH, '//*[@data-id="login-unsuccessful"]')
    delay_response_locator = (By.XPATH, '//*[@data-id="delay"]')
    field_response_status_code_locator = (By.XPATH, '//*[@data-key="response-code"]')
    field_response_body_locator = (By.XPATH, '//*[@data-key="output-response"]')

