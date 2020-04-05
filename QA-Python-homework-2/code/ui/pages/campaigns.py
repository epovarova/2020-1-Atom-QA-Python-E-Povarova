from ui.locators.locators import CampaignsLocators
from .base import BasePage


class CampaignsPage(BasePage):
    locators = CampaignsLocators()

    def go_to_create_campaign(self):
        from .new_campaign import NewCampaignsPage

        try:
            self.click(self.locators.CREATE_CAMPAIGN_EMPTY, 20)
        except Exception:
            self.click(self.locators.CREATE_CAMPAIGN_NOT_EMPTY, 20)
        return NewCampaignsPage(self.driver, self.config)
