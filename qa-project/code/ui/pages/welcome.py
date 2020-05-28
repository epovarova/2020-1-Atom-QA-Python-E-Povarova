from ui.locators.locators import WelcomeLocators
from ui.pages.base import BasePage
from ui.pages.welcome_hrefs import ApiPage, SmtpPage, PopularMechanicsPage, PythonPage, PythonHistoryPage, \
    AboutFlaskPage, DownloadCentosPage, WiresharkDownloadPage, WiresharkNewsPage, TCPDumpExamplesPage


class WelcomePage(BasePage):
    locators = WelcomeLocators

    def go_to_what_is_an_api(self):
        self.click(self.locators.WHAT_IS_AN_API)
        return ApiPage(self.driver, self.config)

    def go_to_future_of_internet(self):
        self.click(self.locators.FUTURE_OF_INTERNET)
        return PopularMechanicsPage(self.driver, self.config)

    def go_to_lets_talk_about_smtp(self):
        self.click(self.locators.LETS_TALK_ABOUT_SMTP)
        return SmtpPage(self.driver, self.config)

    def go_to_python(self):
        self.click(self.locators.PYTHON)
        return PythonPage(self.driver, self.config)

    def go_to_python_history(self):
        self.move_to_element(self.locators.PYTHON)
        self.click(self.locators.PYTHON_HISTORY)
        return PythonHistoryPage(self.driver, self.config)

    def go_to_about_flask(self):
        self.move_to_element(self.locators.PYTHON)
        self.click(self.locators.ABOUT_FLASK)
        return AboutFlaskPage(self.driver, self.config)

    def go_to_download_centos(self):
        self.move_to_element(self.locators.LINUX)
        self.click(self.locators.DOWNLOAD_CENTOS)
        return DownloadCentosPage(self.driver, self.config)

    def go_to_wireshark_news(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.WIRESHARK_NEWS)
        return WiresharkNewsPage(self.driver, self.config)

    def go_to_wireshark_download(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.WIRESHARK_DOWNLOAD)
        return WiresharkDownloadPage(self.driver, self.config)

    def go_to_tcpdump_examples(self):
        self.move_to_element(self.locators.NETWORK)
        self.click(self.locators.TCPDUMP_EXAMPLES)
        return TCPDumpExamplesPage(self.driver, self.config)

    def logout(self):
        from ui.pages.main import MainPage
        self.click(self.locators.LOGOUT)
        return MainPage(self.driver, self.config)
