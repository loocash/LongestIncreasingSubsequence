"""
Longest Increasing Subsequence
"""

import math
from bisect import bisect_right


def lis_naive(xs: list):
    """ O(n^2) """
    longest = [0] * (len(xs) + 1)

    for i, x in enumerate(xs):
        less_than_x = filter(lambda k: xs[k] < x, range(i))
        maxi = max(less_than_x, key=lambda k: longest[k], default=-1)
        longest[i] = longest[maxi] + 1

    return max(longest, default=0)


def lis(xs: list):
    """ O(n lg n) """
    smallest = [math.inf] * (len(xs)+1)
    for x in xs:
        j = bisect_right(smallest, x)
        if j > 0 and smallest[j-1] == x:
            continue
        smallest[j] = x

    return smallest.index(math.inf)
