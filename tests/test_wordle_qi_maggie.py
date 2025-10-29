#!/usr/bin/env python
import pytest

"""Tests for `wordle_qi_maggie` package."""

# from wordle_qi_maggie import wordle_qi_maggie


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyfeldroy/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string

from wordle_qi_maggie import validate_guess, check_guess, is_valid_word, calculate_game_score


def test_validate_guess():
    """Test the validate_guess function"""
    # Valid guesses
    assert validate_guess("apple") == True
    assert validate_guess("tests") == True
    
    # Invalid guesses
    assert validate_guess("APPLE") == False  # uppercase
    assert validate_guess("app") == False    # too short
    assert validate_guess("applepie") == False  # too long
    assert validate_guess("appl3") == False  # contains number
    assert validate_guess(12345) == False    # not a string


def test_check_guess():
    """Test the check_guess function"""
    # Perfect match
    result = check_guess("apple", "apple")
    assert result == [('a', 'green'), ('p', 'green'), ('p', 'green'), ('l', 
    'green'), ('e', 'green')]
    
    # Partial matches
    result = check_guess("apple", "apply")
    assert result == [('a', 'green'), ('p', 'green'), ('p', 'green'), ('l', 
    'green'), ('y', 'gray')]
    
    # Mixed matches
    result = check_guess("apple", "pilot")
    assert result[0][1] == 'yellow'  # p should be yellow
    assert result[2][1] == 'yellow'  # l should be yellow
    
    # Different lengths
    result = check_guess("apple", "app")
    assert result == []


def test_is_valid_word():
    """Test the is_valid_word function"""
    word_list = ["apple", "banana", "cherry", "grape", "orange"]
    
    # Valid words
    assert is_valid_word("apple", word_list) == True
    assert is_valid_word("APPLE", word_list) == True  # case insensitive
    
    # Invalid words
    assert is_valid_word("mango", word_list) == False
    assert is_valid_word("", word_list) == False


def test_calculate_game_score():
    """Test the calculate_game_score function"""
    # Normal cases
    assert calculate_game_score(1, 6) == 6  # solved in 1 guess
    assert calculate_game_score(3, 6) == 4  # solved in 3 guesses
    assert calculate_game_score(6, 6) == 1  # solved in last guess
    
    # Edge cases
    assert calculate_game_score(0, 6) == 0  # invalid input
    assert calculate_game_score(7, 6) == 0  # exceeded max guesses
    assert calculate_game_score(2, 10) == 9  # different max guesses
