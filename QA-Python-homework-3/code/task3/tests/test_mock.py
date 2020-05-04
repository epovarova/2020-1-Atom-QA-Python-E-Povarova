import pytest


class TestMock:

    @pytest.fixture(autouse=True)
    def setup_class(self, setup_mock):
        self.data = setup_mock

    @pytest.mark.MOCK
    def test_post(self, socket_client):
        socket_client.connect()
        info = {'author': 'Mark Twen', 'name': 'The Adventures of Tom Sawyer'}
        socket_client.post('/new_book', info)
        result = socket_client.receive()

        assert result['status_code'] == 200
        assert result['data'] == info
        socket_client.disconnect()

    @pytest.mark.MOCK
    def test_get_by_id(self, socket_client):
        socket_client.connect()
        socket_client.get('/books/0')
        result = socket_client.receive()
        assert result['status_code'] == 200
        assert result['data'] == self.data
        socket_client.disconnect()

    @pytest.mark.MOCK
    def test_get(self, socket_client):
        socket_client.connect()
        socket_client.get('/books')
        result = socket_client.receive()
        assert result['status_code'] == 200
        socket_client.disconnect()

    @pytest.mark.MOCK
    def test_invalid_get(self, socket_client):
        socket_client.connect()
        socket_client.get('/books/100000')
        result = socket_client.receive()
        assert result['status_code'] == 404
        socket_client.disconnect()
