# test_bank.py
# Tests the value() function from bank.py using pytest.

from bank import value

# Tests greetings that start with "hello" (case-insensitive)
def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("HELLO") == 0
    assert value("HELLO THERE") == 0
    assert value("Hello There") == 0


# Tests greetings that start with 'h' but not "hello"
def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("H") == 20
    assert value("HI") == 20


# Tests greetings that do not start with 'h' at all
def test_else():
    assert value("123") == 100
    assert value("Test") == 100
    assert value("TEST") == 100
    assert value("JHSAFFF924") == 100
