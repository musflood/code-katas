"""Kata: Highest Scoring Word.

#1 Best Practices Solution by daddepledge
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
"""


def high(x):
    """Find the highest scoring word in a sentence.

    Words are scored by adding up the value of each of the letters,
    with a = 1, b = 2, c = 3 etc. For words that score the same,
    the earliest word is returned. Sentences must be all lowercase with
    no specail characters.
    """
    if not x:
        return x
    return max(x.split(), key=lambda word: sum(ord(ch) - 96 for ch in word))
