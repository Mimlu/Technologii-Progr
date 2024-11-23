import pytest
from divide import divide

def test_divide_positive_numbers():
    assert divide(6, 2) == 3.0
    assert divide(25, 4) == 6.25


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(21, 0)

def test_divide_negative_numbers():
    assert divide(-20, 2) == -10.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0

def test_rounding():
    assert divide(17, 3) == 5.67
    assert divide(1, 3) == 0.33