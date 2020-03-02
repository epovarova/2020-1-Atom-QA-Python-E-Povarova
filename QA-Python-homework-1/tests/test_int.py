""" Int testing """
import pytest


class TestInt(object):
    """ Class for testing int """

    @staticmethod
    @pytest.fixture(scope="function", params=[(3, 2, 9), (0, 2, 0), (-3, 3, -27)])
    def param_test(request):
        return request.param

    @staticmethod
    def test_pow_with_fixture(param_test):
        (int_for_testing, power, result) = param_test
        assert pow(int_for_testing, power) == result

    @staticmethod
    @pytest.mark.parametrize("int_for_testing, expected", [(5, 5), (0, 0), (-5, 5)])
    def test_abs_with_parametrization(int_for_testing, expected):
        assert abs(int_for_testing) == expected

    @staticmethod
    @pytest.mark.parametrize("int_for_testing, expected", [(1, '0b1'), (0, '0b0'), (20, '0b10100')])
    def test_bin_with_parametrization(int_for_testing, expected):
        assert bin(int_for_testing) == expected

    @staticmethod
    @pytest.mark.parametrize("int_for_testing, divider, expected",
                             [(10, 10, 1), (10, 3, 3), (10, 15, 0)])
    def test_div_with_parametrization(int_for_testing, divider, expected):
        assert int_for_testing // divider == expected

    @staticmethod
    def test_div_by_zero():
        with pytest.raises(ZeroDivisionError):
            10 // 0

