"""Tests for the alt_split module."""
import pytest


ENCRYPTION = [
    ("This is a test!", 0, "This is a test!"),
    ("This is a test!", 1, "hsi  etTi sats!"),
    ("This is a test!", 2, "s eT ashi tist!"),
    ("This is a test!", 3, " Tah itse sits!"),
    ("This is a test!", 4, "This is a test!"),
    ("This is a test!", -1, "This is a test!"),
    ("This kata is very interesting!", 1, "hskt svr neetn!Ti aai eyitrsig"),
]


@pytest.mark.parametrize('text, n', [('', 0), (None, 0), ('', 1), (None, 1)])
def test_encrypt_empty_string(text, n):
    """Test that given '' or None, encrypt returns that value."""
    from alt_split import encrypt
    assert encrypt(text, n) == text


@pytest.mark.parametrize('text, n, result', ENCRYPTION)
def test_encrypt(text, n, result):
    """Test encrypt for proper output."""
    from alt_split import encrypt
    assert encrypt(text, n) == result


DECRYPTION = [
    ("This is a test!", 0, "This is a test!"),
    ("hsi  etTi sats!", 1, "This is a test!"),
    ("s eT ashi tist!", 2, "This is a test!"),
    (" Tah itse sits!", 3, "This is a test!"),
    ("This is a test!", 4, "This is a test!"),
    ("This is a test!", -1, "This is a test!"),
    ("hskt svr neetn!Ti aai eyitrsig", 1, "This kata is very interesting!"),
]


@pytest.mark.parametrize('text, n', [('', 0), (None, 0), ('', 1), (None, 1)])
def test_decrypt_empty_string(text, n):
    """Test that given '' or None, decrypt returns that value."""
    from alt_split import encrypt
    assert encrypt(text, n) == text


@pytest.mark.parametrize('text, n, result', DECRYPTION)
def test_decrypt(text, n, result):
    """Test decrypt for proper output."""
    from alt_split import decrypt
    assert decrypt(text, n) == result
