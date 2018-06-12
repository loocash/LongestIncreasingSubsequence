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
