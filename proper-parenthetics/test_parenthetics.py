"""Tests for the parenthetics module."""
import pytest


@pytest.mark.parametrize('parens', ['', '()', '(())', '()()',
                                    '(2 + 1)(((1+4)/2) - (8**2))', 'a'])
def test_proper_parenthetics_balanced_parens(parens):
    """Test that string with equal open and closed parens is balanced (0)."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(parens) == 0


@pytest.mark.parametrize('parens', ['(', '()(', '(()', '(string',
                                    '(((x+1)/(x-2) + 4)(5)'])
def test_proper_parenthetics_parens_still_open(parens):
    """Test that string with open parens that are not closed is open (1)."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(parens) == 1


@pytest.mark.parametrize('parens', [')', '())', ')))(((', '(x/5)(2+9)*(1-6))',
                                    'string)'])
def test_proper_parenthetics_broken_parens(parens):
    """Test that string with invalid parens is broken (-1)."""
    from parenthetics import proper_parenthetics
    assert proper_parenthetics(parens) == -1
