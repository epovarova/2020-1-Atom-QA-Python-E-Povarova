import pytest

from api.client import Client


@pytest.fixture(scope='function')
def api_client(config):
    return Client(config['username'], config['password'])


@pytest.fixture(scope='function')
def segment():
    return {
        'name': 'testSegmentAPI',
        'relations_count': 1,
        'pass_condition': 1,
        "relations": [{"object_id": 2135243, "object_type": "remarketing_vk_group",
                       "params": {"type": "positive", "source_id": 32041317}}]
    }