"""Kata: Sum of the first nth term of Series.

#1 Best Practices Solution by MMMAAANNN and others
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Sum the first n terms in a harmonic series.

    Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
    """
    tot = 0
    for x in range(n):
        tot += 1.0 / (1 + 3 * x)
    return '{0:.2f}'.format(tot)
