from faker import Faker

from task2.models.models import Base, Log, ClientError, ServerError, BiggestRequest
from task2.mysql_orm_client import MysqlOrmConnection

fake = Faker()


class MysqlOrmBuilder:

    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_logs()
        self.create_client_errors()
        self.create_server_errors()
        self.create_biggest_requests()

    def create_logs(self):
        if not self.engine.dialect.has_table(self.engine, 'logs'):
            Base.metadata.tables['logs'].create(self.engine)

    def create_biggest_requests(self):
        if not self.engine.dialect.has_table(self.engine, 'biggest_requests'):
            Base.metadata.tables['biggest_requests'].create(self.engine)

    def create_client_errors(self):
        if not self.engine.dialect.has_table(self.engine, 'client_errors'):
            Base.metadata.tables['client_errors'].create(self.engine)

    def create_server_errors(self):
        if not self.engine.dialect.has_table(self.engine, 'server_errors'):
            Base.metadata.tables['server_errors'].create(self.engine)

    def add_log(self):
        log = Log(
            address=fake.ipv4(),
            user=fake.word(),
            timestamp=fake.date_time(),
            method=fake.http_method(),
            url=fake.url(),
            status=200,
            user_agent=fake.user_agent()
        )

        self.connection.session.add(log)
        self.connection.session.commit()

        return log

    def add_biggest_request(self, method, url, address, timestamp, size):
        biggest_request = BiggestRequest(
            address=address,
            timestamp=timestamp,
            method=method,
            url=url,
            size=size
        )

        self.connection.session.add(biggest_request)
        self.connection.session.commit()

        return biggest_request

    def add_client_error(self, url, status, count):
        client_error = ClientError(
            url=url,
            status=status,
            count=count
        )

        self.connection.session.add(client_error)
        self.connection.session.commit()

        return client_error

    def add_server_error(self, url, status, count):
        server_error = ServerError(
            url=url,
            status=status,
            count=count
        )

        self.connection.session.add(server_error)
        self.connection.session.commit()

        return server_error
