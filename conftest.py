import string
from random import choice
import json
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.opera import OperaDriverManager


class Constants:
    MAIN_URL = "http://skleptest.pl/"

@pytest.fixture
def generate_password() -> str:
    """Generate password with ten letters, ten digits and ten punctuation e.g. KkQkIGmsVx1530668957(|+$,_('~{"""
    return "".join(choice(string.ascii_letters) for i in range(10)) + \
           "".join(choice(string.digits) for i in range(10)) + \
           "".join(choice(string.punctuation) for i in range(10))


@pytest.fixture
def web_driver(config) -> WebDriver:
    """  This fixture provides to test WebDriver object and close them after test is finish.
    :return: WebDriver instances
    """
    if config['browser'] == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif config['browser'] == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif config['browser'] == 'chromium':
        driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    elif config['browser'] == 'opera':
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
       raise Exception(f'"{config["browser"]}" is not a supported browser')
    driver.maximize_window()
    driver.implicitly_wait(config['wait_time'])
    driver.get(Constants.MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def config():
  with open('config.json') as config_file:
    data = json.load(config_file)
  return data