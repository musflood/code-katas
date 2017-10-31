"""Tests for the string_pyramid module."""

import pytest


SIDE_VIEW = [
    (None, None),
    ('', ''),
    ('*#', ' # \n***'),
    ('abc', '  c  \n bbb \naaaaa'),
    ('xoxo', '   o   \n  xxx  \n ooooo \nxxxxxxx'),
    ('987654321',
     '        1        \n\
       222       \n\
      33333      \n\
     4444444     \n\
    555555555    \n\
   66666666666   \n\
  7777777777777  \n\
 888888888888888 \n\
99999999999999999')
]


@pytest.mark.parametrize('chars, result', SIDE_VIEW)
def test_side_view(chars, result):
    """Test that string_pyramid has correct ourput for 2 characters."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(None) is None


TOP_VIEW = [
    (None, None),
    ('', ''),
    ('*#', '***\n*#*\n***'),
    ('abc',
     '''aaaaa
abbba
abcba
abbba
aaaaa'''),
    ('xoxo',
     '''xxxxxxx
xooooox
xoxxxox
xoxoxox
xoxxxox
xooooox
xxxxxxx
'''),
    ('987654321',
     '''99999999999999999
98888888888888889
98777777777777789
98766666666666789
98765555555556789
98765444444456789
98765433333456789
98765432223456789
98765432123456789
98765432223456789
98765433333456789
98765444444456789
98765555555556789
98766666666666789
98777777777777789
98888888888888889
99999999999999999''')
]


@pytest.mark.parametrize('chars, result', TOP_VIEW)
def test_top_view(chars, result):
    """Test that string_pyramid has correct ourput for 2 characters."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(None) is None


@pytest.mark.parametrize('chars, result', [(None, -1), ('', -1), ('*#', 9),
                                           ('abc', 25), ('xoxo', 49),
                                           ('987654321', 289)])
def test_visible_count(chars, result):
    """Test that string_pyramid has correct ourput for 2 characters."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(None) == -1


@pytest.mark.parametrize('chars, result', [(None, -1), ('', -1), ('*#', 10),
                                           ('abc', 35), ('xoxo', 84),
                                           ('987654321', 969)])
def test_total_count(chars, result):
    """Test that string_pyramid has correct ourput for 2 characters."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(None) == -1
