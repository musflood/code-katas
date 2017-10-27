"""Tests for the highest_word module."""
import pytest


SENTENCES = [
    ('', ''),
    ('man i need a taxi up to ubud', 'taxi'),
    ('what time are we climbing up the volcano', 'volcano'),
    ('take me to semynak', 'semynak'),
    ('i like to play the xylophone on a zebra', 'xylophone'),
    ('a aa aaa aaaa b c d', 'aaaa'),
    ('lqg pxpgmxmbf flrlja yatbk chgqhelv tinojxyloq xxlyue \
      eeuxfyre pwfsci bzhaxnvmkm xhmttddpil vqworv ugiricbkan \
      rbpnjxntfs rmbwewy unegp nsdjo luzmt raysiyg ayi hsjx \
      bitxtmiml bibveaio zivrlyslc odecu', 'tinojxyloq')
]


@pytest.mark.parametrize('x, result', SENTENCES)
def test_high(x, result):
    """Test high for proper output."""
    from highest_word import high
    assert high(x) == result
