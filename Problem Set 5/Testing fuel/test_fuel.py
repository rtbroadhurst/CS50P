# tests the convert() and gauge() functions from fuel.py using pytest

from fuel import convert, gauge
import pytest


# tests valid fraction inputs
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1


# tests invalid fraction inputs
def test_convert_invalid():
    # denominator cannot be zero
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    # X cannot be greater than Y
    with pytest.raises(ValueError):
        convert("5/2")

    # must be integers
    with pytest.raises(ValueError):
        convert("cat/dog")


# tests gauge() output formatting
def test_gauge():
    assert gauge(1) == "E"      # 1% or less: empty
    assert gauge(0) == "E"
    assert gauge(99) == "F"     # 99% or more: full
    assert gauge(100) == "F"
    assert gauge(75) == "75%"   # otherwise: percentage
