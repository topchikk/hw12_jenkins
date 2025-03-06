import allure
import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv


DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "126.0"


def pytest_addoption(parser):
    parser.addoption("--browser_name")
    parser.addoption("--browser_version")

#Загрузка переменных из файла .env
load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_settings(request):
    with allure.step("Параметры браузера"):
        browser_name = request.config.getoption('browser_name') or DEFAULT_BROWSER_NAME
        browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
        options = Options()
        selenoid_capabilities = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
#Для того, чтобы не передавать лог/пас в ссылке
        options.capabilities.update(selenoid_capabilities)
        selenoid_host = os.getenv("SELENOID_HOST")
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@{selenoid_host}/wd/hub",
            options=options)

        browser.config.driver = driver
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        browser.config.base_url = 'https://demoqa.com'
        # browser.config.timeout = 20

        yield

        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)

        browser.quit()