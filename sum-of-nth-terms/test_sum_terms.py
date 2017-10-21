"""Tests for the sum_terms module."""
import pytest


@pytest.mark.parametrize('n, result', [(1, '1.00'), (2, '1.25'), (3, '1.39'),
                         (4, '1.49'), (5, '1.57'), (6, '1.63'), (7, '1.68')])
def test_series_sum(n, result):
    """Test series_sum for proper output."""
    from sum_terms import series_sum
    assert series_sum(n) == result
