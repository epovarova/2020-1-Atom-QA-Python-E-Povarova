from pathlib import Path
from time import sleep

from ui.locators.locators import NewCampaignsLocators
from ui.pages.base import BasePage


class NewCampaignsPage(BasePage):
    locators = NewCampaignsLocators()

    def create_campaign(self, link, name, male=True, female=True, ages=""):
        from ui.pages.campaigns import CampaignsPage

        self.click(self.locators.TRAFFIC)
        self.find(self.locators.LINK_FIELD).send_keys(link)
        self.click(self.locators.CLEAR_NAME_BUTTON, 20)
        self.find(self.locators.NAME_FIELD).send_keys(name)

        self.click(self.locators.SEX_FIELD)
        if not male:
            self.click(self.locators.MALE_CHECKBOX)
        if not female:
            self.click(self.locators.FEMALE_CHECKBOX)

        if ages != "":
            self.click(self.locators.AGE_FIELD)
            self.click(self.locators.AGE_CHOICE)
            self.click(self.locators.RANDOM_AGE)
            self.find(self.locators.AGE_INPUT).clear()
            self.find(self.locators.AGE_INPUT).send_keys(ages)

        self.click(self.locators.FORMAT_TEASER)

        self.find(self.locators.BANNER_TITLE).send_keys("Go to the adventure")
        self.find(self.locators.BANNER_TEXT).send_keys("Do not pass by a unique site!")

        self.find(self.locators.UPLOAD_FILE).send_keys(str(Path("ui/resources/avatar_265008.jpg").resolve()))
        sleep(3)

        self.click(self.locators.ADD_ADVERT)
        self.click(self.locators.CONFIRM_CREATING)
        return CampaignsPage(self.driver, self.config)
