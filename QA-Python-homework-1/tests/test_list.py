""" List testing """
import pytest


class TestList(object):
    """ Class for testing list """

    @staticmethod
    @pytest.fixture()
    def create_list():
        return [i for i in range(10)]

    @staticmethod
    @pytest.fixture(scope="function", params=[
        ([1], 1),
        ([1, 1], 2),
        ([1, 1, 1], 3)
    ])
    def param_test(request):
        return request.param

    @staticmethod
    def test_pop_from_list(create_list):
        list_for_testing = create_list
        list_for_testing.append(1)
        assert list_for_testing.pop() == 1

    @staticmethod
    def test_remove_nonexistent_value(create_list):
        with pytest.raises(ValueError):
            list_for_testing = create_list
            list_for_testing.remove(11)

    @staticmethod
    def test_pop_from_empty_list():
        with pytest.raises(IndexError):
            list_for_testing = []
            list_for_testing.pop(1)

    @staticmethod
    def test_count_with_fixture(param_test):
        (list_for_testing, expected) = param_test
        list_for_testing = list(list_for_testing)
        result = list_for_testing.count(1)
        assert result == expected

    @staticmethod
    @pytest.mark.parametrize("list_for_testing, expected",
                             [([1, 2, 3], [1, 2, 3]), ([3, 2, 1], [1, 2, 3])])
    def test_sort_with_parametrization(list_for_testing, expected):
        list_for_testing.sort()
        assert list_for_testing == expected
