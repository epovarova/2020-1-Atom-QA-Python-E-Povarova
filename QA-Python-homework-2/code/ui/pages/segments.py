from ui.locators.locators import SegmentsLocators
from .base import BasePage
from .vk_groups import VkGroupsPage


class SegmentsPage(BasePage):
    locators = SegmentsLocators()

    def go_to_vk_groups(self):
        self.click(self.locators.VK_GROUPS)
        return VkGroupsPage(self.driver, self.config)

    def go_to_create_segment(self):
        from .new_segment import NewSegmentsPage
        try:
            self.click(self.locators.CREATE_SEGMENT_EMPTY, 20)
        except Exception:
            self.click(self.locators.CREATE_SEGMENT_NOT_EMPTY, 20)
        return NewSegmentsPage(self.driver, self.config)
