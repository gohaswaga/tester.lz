from test import equalize
import pytest

def test_zero():
    assert equalize(0) == "problem with (x - 2 * m.cos(x)) or x = 0"
def test_neg():
    assert equalize(2) ==  "pricol"
def test_type():
    assert equalize("1.029866") == "not number"
def test_float():
    assert equalize(1.3) == 3.4441466128712697
