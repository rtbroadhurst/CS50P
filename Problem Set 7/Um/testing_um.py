from um import count

def test_valid():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...,") == 2


def test_invalid():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("dumb") == 0
    assert count("hummus") == 0


def test_multiple():
    assert count("um um um") == 3
    assert count("Um? Um! Um.") == 3
    assert count("um, um, um, um") == 4
    assert count("UM um Um") == 3


def test_edge_cases():
    assert count("") == 0
    assert count("   ") == 0
    assert count("um") == 1
    assert count("UM") == 1
    assert count("uM") == 1
    assert count("um um") == 2


def test_punctuation_variations():
    assert count("um!") == 1
    assert count("um.") == 1
    assert count("um...") == 1
    assert count("(um)") == 1
    assert count("[um]") == 1
    assert count("\"um\"") == 1
    assert count("um;um") == 2


def test_mixed_with_words():
    assert count("I um don't um know") == 2
    assert count("um, the umbrella, and um") == 2
    assert count("Unfortunately, um, I um agree") == 2
    assert count("UM is a word, um, really?") == 2

