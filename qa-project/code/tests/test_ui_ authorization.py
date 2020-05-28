import allure

from conftest import *
from tests.base import BaseCase
from ui.pages.registration import RegistrationPage
from ui.pages.welcome import WelcomePage


class TestAuthorization(BaseCase):
    faker = Faker()

    @allure.feature('authorization')
    @pytest.mark.UI_AUTH
    def test_positive_login(self, add_user, config):
        name, email = add_user
        assert isinstance(
            self.main_page.login(name, config['default_password']),
            WelcomePage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/authorization/test_positive_login',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('authorization')
    @pytest.mark.UI_AUTH
    def test_negative_login(self, correct_username):
        assert isinstance(
            self.main_page.login(correct_username, 1),
            MainPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/authorization/test_negative_login',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('authorization')
    @pytest.mark.UI_AUTH
    def test_login_with_email(self, add_user, config):
        name, email = add_user
        try:
            assert isinstance(
                self.main_page.login(email, config['default_password']),
                MainPage)
        except:
            pass
        finally:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name='/authorization/test_login_with_email',
                          attachment_type=allure.attachment_type.PNG)

    @allure.feature('authorization')
    @pytest.mark.UI_AUTH
    @pytest.mark.parametrize("username",
                             ['12345', '12345678912345678'])
    def test_login_with_incorrect_name(self, username):
        self.main_page.login(username, 1).find(self.main_page.locators.INCORRECT_USERNAME_LENGTH)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/authorization/test_login_with_incorrect_name',
                      attachment_type=allure.attachment_type.PNG)

    @allure.feature('authorization')
    @pytest.mark.UI_AUTH
    def test_go_to_authorization(self):
        assert isinstance(
            self.main_page.go_to_registration(),
            RegistrationPage)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='/authorization/test_go_to_authorization',
                      attachment_type=allure.attachment_type.PNG)
