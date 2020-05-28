from selenium.common.exceptions import TimeoutException

from ui.locators.locators import RegistrationLocators, WelcomeLocators
from .base import BasePage
from .welcome import WelcomePage


class RegistrationPage(BasePage):
    locators = RegistrationLocators()

    def registration(self, username, email, password, confirm_password, sdet=True):
        self.find(self.locators.USERNAME_FIELD).send_keys(username)
        self.find(self.locators.EMAIL_FIELD).send_keys(email)
        self.find(self.locators.PASSWORD_FIELD).send_keys(password)
        self.find(self.locators.REPEAT_PASSWORD_FIELD).send_keys(confirm_password)

        if sdet:
            self.click(self.locators.SDET_FIELD)
        self.click(self.locators.SUBMIT)

        try:
            welcome_locators = WelcomeLocators()
            self.find(welcome_locators.LOGOUT, 1)
            return WelcomePage(self.driver, self.config)
        except TimeoutException:
            return self
