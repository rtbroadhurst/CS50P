# test_plates.py
# Tests for is_valid() in plates.py

from plates import is_valid


# First two characters must be letters
def test_first_two_characters():
    assert is_valid("CS50")        # valid: starts with letters
    assert not is_valid("1CS50")   # invalid: starts with a digit
    assert not is_valid("C1S50")   # invalid: second character is digit


# Must not contain periods, spaces, or punctuation
def test_periods_spaces_punctuation():
    assert not is_valid("CS 50")   # space invalid
    assert not is_valid("CS-50")   # hyphen invalid
    assert not is_valid("CS.50")   # period invalid
    assert not is_valid("CS!50")   # punctuation invalid


# Numbers cannot appear in the middle
def test_numbers_in_middle():
    assert is_valid("CS50")        # valid: digits only at end
    assert not is_valid("CS50P")   # invalid: letter after digits
    assert not is_valid("AB1C")    # invalid: number enclosed by letters


# Plate length must be between 2 and 6
def test_length_check():
    assert not is_valid("A")       # too short
    assert not is_valid("ABCDEFG") # too long
    assert is_valid("AB")          # minimal valid
    assert is_valid("ABCDEF")      # maximal valid


# Optional rule: all alphanumeric only
def test_alphanumeric():
    assert is_valid("HELLO")       # valid letters only
    assert not is_valid("GO2FAST") # invalid: letters after digits
    assert not is_valid("CS_50")   # underscore invalid
