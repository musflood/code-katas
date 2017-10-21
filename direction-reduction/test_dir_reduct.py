"""Tests for the dir_reduct module."""
import pytest


DIRECTIONS = [
    ([], []),

    (["NORTH", "SOUTH", "EAST", "WEST"], []),

    (["NORTH"], ["NORTH"]),

    (["NORTH", "EAST", "SOUTH", "NORTH", "WEST", "SOUTH"], []),

    (["NORTH", "EAST", "SOUTH", "SOUTH", "NORTH", "WEST", "SOUTH"],
     ["NORTH", "EAST", "SOUTH", "WEST", "SOUTH"]),

    (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"],
     ['WEST']),

    (["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"]),
]


@pytest.mark.parametrize('arr, result', DIRECTIONS)
def test_dir_reduct(arr, result):
    """Test dir_reduct for proper output."""
    from dir_reduct import dir_reduct
    assert dir_reduct(arr) == result
