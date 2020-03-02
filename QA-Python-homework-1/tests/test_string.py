""" String testing """
import pytest


class TestString(object):
    """ Class for testing string """

    @staticmethod
    @pytest.fixture(scope="function", params=[
        ('1', '2', '12'),
        ('1', '', '1'),
        ('', '', '')
    ])
    def param_test(request):
        return request.param

    @staticmethod
    def test_string_immutable():
        with pytest.raises(TypeError):
            string_for_testing = "string"
            string_for_testing[1] = "a"

    @staticmethod
    def test_concat_with_fixture(param_test):
        (first_str, second_str, result) = param_test
        assert first_str + second_str == result

    @staticmethod
    @pytest.mark.parametrize("string_for_testing, expected", [("", ""), ("abc", "abcabc")])
    def test_double_with_parametrization(string_for_testing, expected):
        assert string_for_testing * 2 == expected

    @staticmethod
    @pytest.mark.parametrize("string_for_testing, expected", [("", 0), ("abc", 3)])
    def test_len_with_parametrization(string_for_testing, expected):
        assert len(string_for_testing) == expected

    @staticmethod
    @pytest.mark.parametrize("string_for_testing, expected",
                             [("", False), ("abc", False), ("123abc", False), ("123", True)])
    def test_isdigit_with_parametrization(string_for_testing, expected):
        assert string_for_testing.isdigit() == expected
