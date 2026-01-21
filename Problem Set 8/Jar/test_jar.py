import pytest
from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar(10)
    assert str(jar) == ""

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(5)
