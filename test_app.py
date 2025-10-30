import pytest 
from app import add, multipy, divide

def test_add():
    assert add(3, 5) == 8
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multipy(3, 5) == 15
    assert multipy(2, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(5, 0)

