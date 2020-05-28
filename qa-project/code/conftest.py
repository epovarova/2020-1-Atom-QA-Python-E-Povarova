from faker import Faker

from deploy.mock.mock_client import VkClient
from orm.builder import MysqlOrmBuilder
from orm.models.models import User
from orm.mysql_orm_client import MysqlOrmConnection
from ui.fixtures import *
import pytest


def pytest_addoption(parser):
    parser.addoption('--url', default='http://192.168.17.191:8083/')
    parser.addoption('--username', default='gulkina_liza@mail.ru')
    parser.addoption('--password', default='qwerty123!')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    username = request.config.getoption('--username')
    password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')
    db_user = 'test_qa'
    db_password = 'qa_test'
    db_name = 'MYSQL_DB'

    default_username = "username"
    default_password = "password"
    default_email = "username@example.com"

    mock_host = 'http://192.168.17.191'
    mock_port = 5000

    return {'url': url, 'username': username, 'password': password, 'selenoid': selenoid,
            'db_user': db_user, 'db_password': db_password, 'db_name': db_name,
            'default_username': default_username, 'default_password': default_password, 'default_email': default_email,
            'mock_host': mock_host, 'mock_port': mock_port}


@pytest.fixture(scope='session')
def mysql_orm_client(config):
    return MysqlOrmConnection(config['db_user'], config['db_password'], config['db_name'])


@pytest.fixture(scope='function')
def correct_username():
    faker = Faker()
    username = faker.profile(fields=['username'])['username']
    while len(username) < 6 or len(username) > 16:
        username = faker.profile(fields=['username'])['username']
    return username


@pytest.fixture(scope='session')
def vk_client(config):
    return VkClient("{}:{}".format(config['mock_host'], config['mock_port']))


@pytest.fixture(scope='function')
def add_user(mysql_orm_client, config, correct_username, vk_client):
    faker = Faker()
    current_name = correct_username
    current_email = faker.email()

    builder = MysqlOrmBuilder(mysql_orm_client)
    builder.add_user(current_name, config['default_password'], current_email)
    mysql_orm_client.session.query(User.id).filter_by(username=config['default_username']).all()

    client = vk_client
    client.add_user(current_name, current_name)

    yield current_name, current_email

    builder.delete_user_by_email(current_email)
