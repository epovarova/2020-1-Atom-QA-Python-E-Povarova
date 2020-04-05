from .base import BasePage
from .campaigns import CampaignsPage
from .invalid_auth import InvalidAuthPage
from ui.locators.locators import MainPageLocators, InvalidAuthLocators
from selenium.common.exceptions import TimeoutException


class MainPage(BasePage):
    locators = MainPageLocators()

    def login(self, username, password):
        invalid_auth_locators = InvalidAuthLocators()
        self.click(self.locators.LOGIN_BUTTON)
        self.find(self.locators.LOGIN_FIELD).send_keys(username)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.click(self.locators.CONFIRM_LOGIN)
        try:
            self.find(invalid_auth_locators.INVALID_LOGIN)
            return InvalidAuthPage(self.driver, self.config)
        except TimeoutException:
            return CampaignsPage(self.driver, self.config)
