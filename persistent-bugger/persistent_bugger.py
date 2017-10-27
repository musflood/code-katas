"""Kata: Persistent Bugger.

#1 Best Practices Solution by eyaltra and Silver-Core
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
"""


def persistence(n):
    """Calculate the multiplicative persistence of n.

    The multiplicative persistence of a number, n, is the
    number of times you must multiply the digits in n until
    you reach a single digit
    """
    p = 0
    digits = str(n)
    if len(digits) == 1:
        return p
    while len(digits) > 1:
        digits = str(product(digits))
        p += 1
    return p


def product(nums):
    """Calculate the product of the sequence of digits."""
    tot = 1
    for n in nums:
        tot *= int(n)
    return tot
