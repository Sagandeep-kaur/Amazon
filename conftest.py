# Run Selenium tests by giving browser options on command terminal using pytest
# we can run all tests on any browser by mentioning browser name on terminal
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.options import Options as InternetExplorerOptions
from selenium.webdriver.chrome.options import Options as MicrosoftEdgeOptions
from selenium.webdriver.chrome.options import Options as FirefoxOptions



def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default="chrome")


@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
       browser = webdriver.Chrome()


    elif browser_name == 'firefox':
        browser = webdriver.Firefox()

    browser.get("https://www.amazon.in")
    browser.maximize_window()
    wait = WebDriverWait(browser, 20)
    request.cls.browser = browser
    request.cls.wait = wait
    yield
    browser.close()



