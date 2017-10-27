"""Kata: Simple Encryption #1 - Alternating Split.

#1 Best Practices Solution by damjan and others
def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
"""


def decrypt(encrypted_text, n):
    """Dencrypt a string encypted by alternating the letters n times.

    If the input-string is null or empty or n is <= 0 then the input
    text itself is returned.
    """
    if not encrypted_text:
        return encrypted_text

    text = encrypted_text
    for _ in range(n):
        even_ch = text[:int(len(text) / 2)]
        odd_ch = text[int(len(text) / 2):]
        text = ''
        for i in range(len(even_ch)):
            text += odd_ch[i] + even_ch[i]
        if len(odd_ch) > len(even_ch):
            text += odd_ch[-1]
    return text


def encrypt(text, n):
    """Encrypt a string by alternating the letters n times.

    Alternating is done by taking every 2nd char from the string,
    then the other chars, that are not every 2nd char, and concating
    them as new String.
    If the input-string is null or empty or n is <= 0 then the input
    text itself is returned.
    """
    if not text:
        return text

    encrypted_text = text
    for _ in range(n):
        even_ch = [ch for i, ch in enumerate(encrypted_text) if i % 2]
        odd_ch = [ch for i, ch in enumerate(encrypted_text) if not i % 2]
        encrypted_text = ''.join(even_ch) + ''.join(odd_ch)
    return encrypted_text
