""" Set testing """
import pytest


class TestSet(object):
    """ Class for testing set """

    @staticmethod
    @pytest.fixture()
    def create_set():
        return {i for i in range(10)}

    @staticmethod
    def test_remove_from_set(create_set):
        set_for_testing = create_set
        set_for_testing.remove(9)
        assert {i for i in range(9)} == set_for_testing

    @staticmethod
    def test_remove_nonexistent_value(create_set):
        with pytest.raises(KeyError):
            set_for_testing = create_set
            set_for_testing.remove(11)

    @staticmethod
    def test_clear(create_set):
        set_for_testing = create_set
        set_for_testing.clear()
        assert set_for_testing == set()

    @staticmethod
    def test_copy(create_set):
        set_for_testing = create_set
        assert set_for_testing.copy() == set_for_testing

    @staticmethod
    @pytest.mark.parametrize("other_set, expected",
                             [({9, 10, 11}, {9}), ({10, 11}, set()), (set(), set())])
    def test_intersection_with_parametrization(other_set, expected, create_set):
        set_for_testing = create_set
        assert set_for_testing.intersection(other_set) == expected
