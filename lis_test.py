import unittest
from lis import lis_naive, lis
from collections import namedtuple

Test = namedtuple('Test', 'xs, want')

tests = [
    Test([], 0),
    Test([1], 1),
    Test([1, 2, 3, 4, 5], 5),
    Test([5, 4, 3, 2, 1], 1),
    Test([2, 1, 3, 5, 4], 3),
    Test([1, 1, 1], 1),
    Test([10, 22, 9, 33, 21, 50, 41, 60, 80], 6),
    Test([2, 5, 9, 1, 8, 0, 6, 3, 4, 7], 4),
    Test([6, 0, 2, 7, 5, 8, 1, 3, 9, 4], 5),
    Test([9, 6, 7, 2, 5, 3, 1, 0, 8, 4], 3),
    Test([1, 5, 6, 7, 9, 0, 4, 3, 2, 8], 5),
    Test([5, 3, 0, 4, 9, 12, 19, 11, 15, 18, 7, 6, 17, 2, 13, 16, 1, 8, 14, 10], 6),
    Test([12, 3, 14, 9, 4, 6, 11, 7, 10, 5, 0, 19, 13, 8, 1, 2, 18, 17, 15, 16], 8),
    Test([19, 12, 2, 4, 6, 0, 10, 3, 7, 8, 15, 9, 1, 11, 18, 14, 5, 17, 13, 16], 9),
]

algorithms = [
    lis_naive,
    lis,
]


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        for fn in algorithms:
            for test in tests:
                got = fn(test.xs)
                self.assertEqual(test.want, got, f"{fn.__name__} {test}")


if __name__ == '__main__':
    unittest.main()
