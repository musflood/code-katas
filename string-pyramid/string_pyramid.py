"""Kata: String Pyramid.

#1 Best Practices Solution by zebulan
def watch_pyramid_from_the_side(characters):
    if not characters:
        return characters
    width = 2 * len(characters) - 1
    output = '{{:^{}}}'.format(width).format
    return '\n'.join(output(char * dex) for char, dex in
                     zip(reversed(characters), xrange(1, width + 1, 2)))


def watch_pyramid_from_above(characters):
    if not characters:
        return characters
    width = 2 * len(characters) - 1
    dex = width - 1
    result = []
    for a in xrange(width):
        row = []
        for b in xrange(width):
            minimum, maximum = sorted((a, b))
            row.append(characters[min(abs(dex - maximum), abs(0 - minimum))])
        result.append(''.join(row))
    return '\n'.join(result)


def count_visible_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    return (2 * len(characters) - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    if not characters:
        return -1
    return sum(a ** 2 for a in xrange(1, 2 * len(characters), 2))
"""


def watch_pyramid_from_the_side(characters):
    """Side view of a pyramid where each row is a char in the given string.

                                            a
    watch_pyramid_from_the_side('abc') =>  bbb
                                          ccccc
    """
    if not characters:
        return characters
    pyramid = ''
    width = 1 + 2 * (len(characters) - 1)
    row_width = 1
    for ch in characters[::-1]:
        pyramid += '{:^{width}}\n'.format(ch * row_width, width=width)
        row_width += 2
    return pyramid[:-1]


def watch_pyramid_from_above(characters):
    """Top view of a pyramid where each row is a char in the given string.

                                       ccccc
                                       cbbbc
    watch_pyramid_from_above('abc') => cbabc
                                       cbbbc
                                       ccccc
    """
    if not characters:
            return characters
    pyramid = []
    row_width = 1 + 2 * (len(characters) - 1)
    edge = ''
    for ch in characters:
        pyramid.append('{}{}{}'.format(edge, ch * row_width, edge[::-1]))
        edge += ch
        row_width -= 2
    pyramid.extend(pyramid[-2::-1])
    return '\n'.join(pyramid)


def count_visible_characters_of_the_pyramid(characters):
    """Count the number of visible blocks in the pyramid."""
    if not characters:
        return -1
    return (1 + 2 * (len(characters) - 1)) ** 2


def count_all_characters_of_the_pyramid(characters):
    """Count the total number of blocks in the pyramid."""
    if not characters:
        return -1
    width = 1 + 2 * (len(characters) - 1)
    return sum(n**2 for n in range(1, width + 1, 2))
