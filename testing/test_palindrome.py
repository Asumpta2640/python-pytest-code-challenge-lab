import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize("input_string, expected", [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
])
def test_basic_cases(input_string, expected):
    result = longest_palindromic_substring(input_string)
    assert result in expected


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcde")
    assert len(result) == 1


def test_even_length_palindrome():
    assert longest_palindromic_substring("abba") == "abba"


def test_odd_length_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"


def test_invalid_input_type():
    with pytest.raises(TypeError):
        longest_palindromic_substring(1234)