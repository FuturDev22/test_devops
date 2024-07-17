import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, edge, firefox, or browserstack")
    parser.addoption("--use-grid", action="store", default="local", help="Choose grid: local or browserstack")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    grid = request.config.getoption("--use-grid")

    if grid == "local":
        if browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--start-maximized")
            my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=chrome_options
            )
        elif browser == "edge":
            edge_options = EdgeOptions()
            edge_options.use_chromium = True
            edge_options.add_argument("--inprivate")
            edge_options.add_argument("--start-maximized")
            my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=edge_options
            )
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--private-window")
            firefox_options.add_argument("--start-maximized")
            my_driver = webdriver.Remote(
                command_executor="http://selenium-hub:4444/wd/hub",
                options=firefox_options
            )
        else:
            raise ValueError(f"Unknown browser '{browser}'")
    elif grid == "browserstack":
        browserstack_options = {
            "os": "Windows",
            "osVersion": "10",
            "projectName": "My Project",
            "buildName": "Build 1",
            "sessionName": "Session 1",
            "local": "false",
            "seleniumVersion": "4.0.0"
        }
        if browser == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.set_capability('bstack:options', browserstack_options)
            my_driver = webdriver.Remote(
                command_executor='https://souissioumaima_YPT8ly:Fuzgb1pKwpUxisivkjmj@hub-cloud.browserstack.com/wd/hub',
                options=chrome_options
            )
        elif browser == "edge":
            edge_options = EdgeOptions()
            edge_options.set_capability('bstack:options', browserstack_options)
            my_driver = webdriver.Remote(
                command_executor='https://souissioumaima_YPT8ly:Fuzgb1pKwpUxisivkjmj@hub-cloud.browserstack.com/wd/hub',
                options=edge_options
            )
        elif browser == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.set_capability('bstack:options', browserstack_options)
            my_driver = webdriver.Remote(
                command_executor='https://souissioumaima_YPT8ly:Fuzgb1pKwpUxisivkjmj@hub-cloud.browserstack.com/wd/hub',
                options=firefox_options
            )
        else:
            raise ValueError(f"Unknown browser '{browser}'")
    else:
        raise ValueError(f"Unknown grid '{grid}'")
    
    yield my_driver
    my_driver.quit()
