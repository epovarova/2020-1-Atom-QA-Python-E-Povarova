import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from ui.pages.base import BasePage
from ui.pages.campaigns import CampaignsPage
from ui.pages.main import MainPage


@pytest.fixture(scope='function')
def auth(driver, config):
    main_page = MainPage(driver, config)
    main_page.click(main_page.locators.LOGIN_BUTTON)
    main_page.find(main_page.locators.LOGIN_FIELD).send_keys(config['username'])
    main_page.find(main_page.locators.PASSWORD_FIELD).send_keys(config['password'])
    main_page.click(main_page.locators.CONFIRM_LOGIN)
    return CampaignsPage(driver, config['username'])


@pytest.fixture(scope='function')
def base_page(driver, config):
    return BasePage(driver, config)


@pytest.fixture(scope='function')
def main_page(driver, config):
    return MainPage(driver, config)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    selenoid = config['selenoid']

    if not selenoid:
        manager = ChromeDriverManager(version='80.0.3987.16')
        driver = webdriver.Chrome(executable_path=manager.install())
    else:
        capabilities = {
            'browserName': "chrome",
            'version': '80.0'
        }
        options = ChromeOptions()
        driver = webdriver.Remote(command_executor=selenoid,
                                  options=options,
                                  desired_capabilities=capabilities)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()
