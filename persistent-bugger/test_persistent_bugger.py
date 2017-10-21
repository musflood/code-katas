"""Tests for the persistent_bugger module."""
import pytest


@pytest.mark.parametrize('n, result', [(39, 3), (4, 0), (25, 2), (999, 4),
                                       (0, 0), (1230, 1), (1234, 2),
                                       (9999999, 5)])
def test_persistence(n, result):
    """Test persistence for proper output."""
    from persistent_bugger import persistence
    assert persistence(n) == result


@pytest.mark.parametrize('nums, result', [('0', 0), ('1', 1), ('25', 10),
                                          ('999999', 531441)])
def test_product_of_sequence(nums, result):
    """Test product for proper output."""
    from persistent_bugger import product
    assert product(nums) == result
