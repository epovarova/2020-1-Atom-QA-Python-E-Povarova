import time

import pytest

from task2.mysql_orm_client import MysqlOrmConnection
from task3 import mock_server
from task3.socket_client import SocketClient
from task4.remote_commands import SSH


@pytest.fixture(scope='session')
def config():
    db_user = 'test_user'
    db_password = 'password'
    db_name = 'TEST_PYTHON'

    mock_host = '127.0.0.1'
    mock_port = 5000

    ssh_host = '192.168.17.165'
    ssh_port = 2022
    ssh_user = 'liza'
    ssh_password = 'liza'
    nginx_port = 2080

    return {'db_user': db_user, 'db_password': db_password, 'db_name': db_name,
            'mock_host': mock_host, 'mock_port': mock_port,
            'ssh_host': ssh_host, 'ssh_port': ssh_port, 'ssh_user': ssh_user, 'ssh_password': ssh_password,
            'nginx_port': nginx_port}


@pytest.fixture(scope='session')
def mock(config, socket_client):
    mock_server.run_mock(config['mock_host'], config['mock_port'])

    server_mock_host = config['mock_host']
    server_port = config['mock_port']

    yield server_mock_host, server_port

    socket_client.connect()
    socket_client.get('/shutdown')
    socket_client.disconnect()


@pytest.fixture(scope='session')
def socket_client(config):
    return SocketClient(config['mock_host'], config['mock_port'])


@pytest.fixture(scope='session')
def setup_mock(mock, socket_client):
    data = {'author': 'Mario Puzo', 'name': 'The Godfather'}
    time.sleep(1)
    socket_client.connect()
    socket_client.post('/new_book', data)

    yield data

    socket_client.disconnect()


@pytest.fixture(scope='session')
def mysql_orm_client(config):
    return MysqlOrmConnection(config['db_user'], config['db_password'], config['db_name'])


@pytest.fixture(scope='session')
def ssh_client(config):
    with SSH(hostname=config['ssh_host'], port=config['ssh_port'], username=config['ssh_user'],
             password=config['ssh_password']) as mock_host:
        yield mock_host

@pytest.fixture()
def enable_nginx_port(config, ssh_client):
    if f'{config["nginx_port"]}/tcp' not in ssh_client.exec_root_cmd('firewall-cmd --list-all', config['ssh_password']):
        commands = [
            f'firewall-cmd --permanent --zone=public --add-port={config["nginx_port"]}/tcp',
            'firewall-cmd --reload',
            'systemctl restart nginx'
        ]
        for command in commands:
            ssh_client.exec_root_cmd(command, config['ssh_password'])

