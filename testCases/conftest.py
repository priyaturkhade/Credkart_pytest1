import pytest
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption("--browser") # Now --browser is recognized to your pytest/python


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser") # --browser(agr) will get value for browser e.g chrome, firefox, edge
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in/login")
    yield driver
    driver.quit()

# driver.close vs driver.quit
