"""Tests for the social_golfers module."""
import pytest


@pytest.mark.parametrize('a', [[], [[]], [[], []], [[], [], []]])
def test_empty_groups_are_valid(a):
    """Test that empty solution is valid."""
    from social_golfers import valid
    assert valid(a)


VALID_A = [

    [["AB"]],

    [["AB", "CD"],
     ["AD", "BC"],
     ["BD", "AC"]],

    [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
     ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
     ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
     ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
     ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']],

    [['BACD', 'EFGH', 'IJKL', 'MNOP', 'QRTS'],
     ['AGKO', 'TPIB', 'CFMS', 'DHJR', 'NQEL'],
     ['ALHP', 'BKNS', 'CEOR', 'QDIF', 'GJMT'],
     ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
     ['AFJN', 'RMLB', 'CQPG', 'DEKT', 'HIOS']]

]


@pytest.mark.parametrize('a', VALID_A)
def test_positive_tests(a):
    """Test that certain cases are true."""
    from social_golfers import valid
    assert valid(a)


INVALID_A = [

    [["AB", "CD", "EF", "GH"],
     ["AC", "BD", "EG", "FH"],
     ["AD", "CE"],
     ["AE", "BG", "CH", "FD"]],

    [['AB', 'CD', 'EF', 'GH'],
     ['AC', 'BD', 'EG', 'FH'],
     ['AD', 'CE', '', 'B'],
     ['AE', 'BG', 'CH', 'FD']],

    [["ABC", "DEF"],
     ["ADE", "CBF"]],

    [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
     ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
     ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
     ['AHLP', 'BKNS', 'CEOR', 'DFXQ', 'GJMT'],
     ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']],

    [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
     ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
     ['AGKO', 'BIPT', 'CJMS', 'DHFR', 'ELNQ'],
     ['AHLP', 'NKBS', 'CEOR', 'DFIQ', 'MJGT'],
     ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]

]


@pytest.mark.parametrize('a', INVALID_A)
def test_negative_tests(a):
    """Test that certain cases are false."""
    from social_golfers import valid
    assert not valid(a)
