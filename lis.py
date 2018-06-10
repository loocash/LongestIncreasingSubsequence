"""
Longest Increasing Subsequence
"""


def longest_increasing_subsequence(xs: list):
    longest = [1 for _ in range(len(xs)+1)]
    longest[-1] = 0

    for i, x in enumerate(xs):
        less_than_x = filter(lambda k: xs[k] < x, range(i))
        maxi = max(less_than_x, key=lambda k: longest[k], default=-1)
        longest[i] = longest[maxi] + 1

    return max(longest, default=0)
