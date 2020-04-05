import pytest
from api.urls.urls import Urls
from api.fixtures import *


class TestApi:
    @pytest.mark.API
    def test_positive_login(self, api_client):
        assert api_client.location_after_auth(api_client.user, api_client.password) == Urls.SUCCESS_AUTH

    @pytest.mark.API
    def test_negative_login(self, api_client):
        assert api_client.location_after_auth("123123123", "qwerty123!") == Urls.FAILURE_AUTH

    @pytest.mark.API
    def test_create_segment(self, api_client, segment):
        api_client.login()
        assert api_client.create(segment).status_code == 200

    @pytest.mark.API
    def test_delete_segment(self, api_client, segment):
        api_client.login()
        id = api_client.create(segment).json()['id']
        assert api_client.delete(id) == 204