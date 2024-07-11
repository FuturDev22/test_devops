import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, edge or firefox")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        try:
            my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=chrome_options
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize Chrome WebDriver: {e}")
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("--inprivate")
        edge_options.add_argument("--start-maximized")
        try:
           my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=edge_options
           )
        except Exception as e:
            raise ValueError(f"Failed to initialize Edge WebDriver: {e}")
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--private-window")
        firefox_options.add_argument("--start-maximized")
        try:
            my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=firefox_options
            )
        except Exception as e:
            raise ValueError(f"Failed to initialize Firefox WebDriver: {e}")
    else:
        raise ValueError(f"Unknown browser '{browser}'")
    
    yield my_driver
    my_driver.quit()




