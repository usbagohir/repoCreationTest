import pytest
from math_functions  import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(5.1, 5) == 10.1

def test_sub():
    assert sub(1, 2) == -1
    assert sub(-1, 1) == -2
    assert sub(5.1, 5) == 0.1

def test_mul():
    assert mul(1, 2) == 2
    assert mul(-1, 1) == -1
    assert mul(5.1, 0) == 0
    assert mul(1.1, 2) == 2.2

def test_div():
    assert div(1, 2) == 0.5
    assert div(-1, 1) == -1
    assert div(1.1, 1) == 1.1
def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)