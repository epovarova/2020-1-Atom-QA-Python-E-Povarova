from conftest import *
from tests.base import BaseCase


class Test(BaseCase):

    @pytest.mark.UI
    def test_positive_login_with_fixture(self, auth):
        page_after_login = auth
        page_after_login.find(page_after_login.locators.USER_TITLE(self.config['username']))

    @pytest.mark.UI
    def test_positive_login(self):
        page_after_login = self.main_page.login("gulkina_liza@mail.ru", "qwerty123!")
        page_after_login.find(page_after_login.locators.USER_TITLE(self.config['username']))

    @pytest.mark.UI
    def test_negative_login(self):
        page_after_login = self.main_page.login("123123123", "qwerty123!")
        page_after_login.find(page_after_login.locators.INVALID_LOGIN)

    @pytest.mark.UI
    def test_create_campaign(self, auth):
        link = "https://fatcatart.com/"
        name = "test campaign for {}".format(link)

        page_after_login = auth
        creation_page = page_after_login.go_to_create_campaign()
        page_with_campaign = creation_page.create_campaign(link, name, ages="20-30")
        page_with_campaign.find(page_after_login.locators.CAMPAIGN_NAME(name)).is_displayed()

    @pytest.mark.UI
    def test_create_segment(self, auth):
        group_name = "Лентач"
        segment_name = "testSegment"

        page_after_login = auth
        vk_groups_page = page_after_login.go_to_segments().go_to_vk_groups()
        vk_groups_page.add_group(group_name)

        creation_page = vk_groups_page.go_to_segments().go_to_create_segment()
        page_with_segment = creation_page.create_segment(group_name, segment_name)
        page_with_segment.find(page_with_segment.locators.SEGMENT_NAME(segment_name)).is_displayed()

    @pytest.mark.UI
    def test_delete_segment(self, auth):
        group_name = "Лентач"
        segment_name = "testSegment"

        page_after_login = auth
        creation_page = page_after_login.go_to_segments().go_to_create_segment()
        page_with_segment = creation_page.create_segment(group_name, segment_name)
        page_with_segment.find(page_with_segment.locators.SEGMENT_NAME(segment_name)).is_displayed()

        page_with_segment.click(page_with_segment.locators.SORT_BY_ID)
        count_before_delete = page_with_segment.count_elements(page_with_segment.locators.SEGMENT_NAME(segment_name))
        page_with_segment.click(page_with_segment.locators.DELETE(segment_name))
        page_with_segment.click(page_with_segment.locators.CONFIRM_DELETE, 10)

        count_after_delete = page_with_segment.count_elements(page_with_segment.locators.SEGMENT_NAME(segment_name))

        assert ++count_after_delete == count_before_delete
