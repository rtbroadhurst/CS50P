from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_invalid():
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False
    assert validate("cat") == False
    