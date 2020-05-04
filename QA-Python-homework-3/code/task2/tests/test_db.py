import datetime
import os

import pytest

from task1.parser import Parser
from task2.models.models import Log, ClientError, ServerError, BiggestRequest
from task2.tests.builder import MysqlOrmBuilder


class TestOrmMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql = mysql_orm_client
        self.builder = MysqlOrmBuilder(mysql_orm_client)
        self.parser = Parser()
        self.biggest_request, self.client_error, self.server_error = self.parser.analyze_file(
            os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'resources', 'access.log')),
            "db")

    @pytest.mark.ORM
    def test_logs_delete(self):
        for _ in range(10):
            self.builder.add_log()

        res = self.mysql.session.query(Log).filter_by(id=10)
        res.delete()
        self.mysql.session.commit()

        self.mysql.session.query(Log).delete()
        self.mysql.session.commit()

    @pytest.mark.ORM
    def test_biggest_request_insert(self):
        for biggest_request in self.biggest_request:
            splitted = biggest_request[1].split()
            timestamp = str(splitted[3] + splitted[4]).replace('[', "").replace(']', "")
            self.builder.add_biggest_request(splitted[0], splitted[1], splitted[2],
                                             datetime.datetime.strptime(timestamp, '%d/%b/%Y:%H:%M:%S%z'),
                                             biggest_request[0])

        res = self.mysql.session.query(BiggestRequest).all()
        if len(self.biggest_request) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.biggest_request)

    @pytest.mark.ORM
    def test_client_error_insert(self):
        for client_error in sorted(self.client_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
            self.builder.add_client_error(client_error[0].split(sep=':')[0],
                                          int(client_error[0].split(sep=':')[1]),
                                          client_error[1])

        res = self.mysql.session.query(ClientError).all()
        if len(self.client_error) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.client_error)

    @pytest.mark.ORM
    def test_server_error_insert(self):
        for server_error in sorted(self.server_error.items(), key=lambda kv: kv[1], reverse=True)[:10]:
            self.builder.add_server_error(server_error[0].split(sep=':')[0],
                                          int(server_error[0].split(sep=':')[1]),
                                          server_error[1])

        res = self.mysql.session.query(ServerError).all()
        if len(self.server_error) > 10:
            assert len(res) == 10
        else:
            assert len(res) == len(self.server_error)
