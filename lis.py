"""
Longest Increasing Subsequence
"""


def lis_naive(xs: list):
    """ O(n^2) """
    longest = [0] * (len(xs)+1)

    for i, x in enumerate(xs):
        less_than_x = filter(lambda k: xs[k] < x, range(i))
        maxi = max(less_than_x, key=lambda k: longest[k], default=-1)
        longest[i] = longest[maxi] + 1

    return max(longest, default=0)
