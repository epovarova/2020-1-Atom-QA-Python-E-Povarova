from selenium.common.exceptions import TimeoutException

from ui.locators.locators import VkGroupsLocators
from .base import BasePage


class NonexistentGroup(Exception):
    pass


class VkGroupsPage(BasePage):
    locators = VkGroupsLocators()

    def add_group(self, name):
        self.find(self.locators.LINK_FIELD).send_keys(name)
        try:
            self.click(self.locators.FIRST_SUGGEST)
        except TimeoutException:
            raise NonexistentGroup

        self.find(self.locators.GROUP_NAME_IN_TABLE(name))
