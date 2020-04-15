from ui.fixtures import *
import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--username', default='gulkina_liza@mail.ru')
    parser.addoption('--password', default='qwerty123!')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')

    return {'url': url, 'username': username, 'password': password, 'selenoid': selenoid}