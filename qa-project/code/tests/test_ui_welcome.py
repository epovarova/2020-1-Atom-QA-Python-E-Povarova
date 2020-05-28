import allure

from conftest import *
from tests.base import BaseCase
from ui.pages.welcome import WelcomePage
from ui.pages.welcome_hrefs import ApiPage, SmtpPage, PopularMechanicsPage, PythonPage, PythonHistoryPage, \
    AboutFlaskPage, DownloadCentosPage, WiresharkDownloadPage, WiresharkNewsPage, TCPDumpExamplesPage


class TestWelcome(BaseCase):

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_what_is_an_api(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_what_is_an_api(), ApiPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_future_of_internet(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_future_of_internet(), PopularMechanicsPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_lets_talk_about_smtp(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_lets_talk_about_smtp(), SmtpPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_python(), PythonPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python_history(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_python_history(), PythonHistoryPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_python_history(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_python_history(), PythonHistoryPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_about_flask(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_about_flask(), AboutFlaskPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_download_centos(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_download_centos(), DownloadCentosPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_wireshark_news(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_wireshark_news(), WiresharkNewsPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_wireshark_download(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_wireshark_download(), WiresharkDownloadPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_tcpdump_examples(self, auth):
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.go_to_tcpdump_examples(), TCPDumpExamplesPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('welcome')
    @pytest.mark.UI_WEL
    def test_logout(self, auth):
        from ui.pages.main import MainPage
        welcome_page: WelcomePage = auth
        assert isinstance(welcome_page.logout(), MainPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/registration/test_registration_existing_user',
                      attachment_type=allure.attachment_type.PNG)
