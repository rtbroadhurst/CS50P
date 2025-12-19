from jar import CookieJar
import pytest

def test_deposit_valid():
    jar = CookieJar()
    jar.deposit(3)
    assert jar.size == 3

def test_deposit_invalid():
    jar = CookieJar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw_valid():
    jar = CookieJar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

def test_withdraw_invalid():
    jar = CookieJar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)

def test_sequence():
    jar = CookieJar()
    jar.deposit(12)
    jar.withdraw(2)
    jar.deposit(1)
    assert jar.size == 11

def test_str():
    jar = CookieJar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_negative_amounts():
    jar = CookieJar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)

def test_init_invalid_capacity():
    with pytest.raises(ValueError):
        CookieJar(-1)
