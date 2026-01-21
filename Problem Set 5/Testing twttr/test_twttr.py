# tests the shorten() function from twttr.py using pytest

from twttr import shorten

def test_shorten():
    assert shorten("twitter") == "twttr"      # basic lowercase input
    assert shorten("TWITTER") == "TWTTR"      # basic uppercase input
    assert shorten("AEIOUaeiou") == ""        # all vowels   
    assert shorten("Hello, world!") == "Hll, wrld!"  # uses punctuation and spaces

    