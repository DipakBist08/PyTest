import pytest
import sourcePackage.source_functions as my_function


def test_addition():
    result = my_function.addition(10, 2)
    assert result == 12


def test_subtraction():
    result = my_function.subtraction(101, 100)
    assert result == 1


def test_multiplication():
    result = my_function.multiplication(25, 5)
    assert result == 125


def test_division():
    result = my_function.division(100, 5)
    assert result == 20


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_function.division(14, 0)


# To test strings
def test_string_Values():
    result = my_function.addition("I Like ", "MacBook Pro")
    assert result == 'I Like MacBook Pro'
