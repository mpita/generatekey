import math
import string

import pytest

from generatekey import generate_user_password, get_secret_key


def test_get_secret_key_default():
    """Test get_secret_key with default parameters."""
    key = get_secret_key()
    assert isinstance(key, str)
    expected_length = 4 * math.ceil(64 / 3)
    assert len(key) == expected_length


def test_get_secret_key_custom_length():
    """Test get_secret_key with custom nbytes."""
    nbytes = 32
    key = get_secret_key(nbytes)
    assert isinstance(key, str)
    expected_length = 4 * math.ceil(nbytes / 3)
    assert len(key) == expected_length


def test_get_secret_key_invalid_nbytes():
    """Test get_secret_key raises ValueError with invalid nbytes."""
    with pytest.raises(ValueError):
        get_secret_key(nbytes=-1)
    with pytest.raises(ValueError):
        get_secret_key(nbytes=0)


def test_generate_user_password_default():
    """Test generate_user_password with default parameters."""
    password = generate_user_password()
    assert isinstance(password, str)
    assert len(password) == 12


def test_generate_user_password_custom_length():
    """Test generate_user_password with custom length."""
    length = 16
    password = generate_user_password(length)
    assert isinstance(password, str)
    assert len(password) == length


def test_generate_user_password_invalid_length():
    """Test generate_user_password raises ValueError with invalid length."""
    with pytest.raises(ValueError):
        generate_user_password(length=-1)
    with pytest.raises(ValueError):
        generate_user_password(length=0)


def test_generate_user_password_characters():
    """Test that the password contains expected character types."""
    password = generate_user_password(100)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_punct = any(c in string.punctuation for c in password)
    assert has_upper
    assert has_lower
    assert has_digit
    assert has_punct
