import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from api.api_data.data_url import base_url


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get(url=base_url)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
