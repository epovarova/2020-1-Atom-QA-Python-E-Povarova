""" Dictionary testing """
import pytest


class TestDict(object):
    """ Class for testing dictionary """

    @staticmethod
    @pytest.fixture()
    def create_dict():
        return {i: i ** 2 for i in range(10)}

    @staticmethod
    def test_get_nonexistent_value(create_dict):
        dict_for_testing = create_dict
        assert dict_for_testing.get(10) is None

    @staticmethod
    def test_get_nonexistent_value_with_default(create_dict):
        dict_for_testing = create_dict
        assert dict_for_testing.get(10, 1) == 1

    @staticmethod
    def test_clear(create_dict):
        dict_for_testing = create_dict
        dict_for_testing.clear()
        assert dict_for_testing == {}

    @staticmethod
    def test_copy(create_dict):
        dict_for_testing = create_dict
        assert dict_for_testing.copy() == dict_for_testing

    @staticmethod
    @pytest.mark.parametrize("dict_for_testing, expected",
                             [({1: 1, 2: 2, 3: 3}, [1, 2, 3]), ({1: 'one', 2: 'two'}, ['one', 'two']), ({}, [])])
    def test_values_with_parametrization(dict_for_testing, expected):
        assert list(dict_for_testing.values()) == expected
