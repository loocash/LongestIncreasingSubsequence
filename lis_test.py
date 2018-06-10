import unittest
from lis import longest_increasing_subsequence
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


class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_longest_increasing_subsequence(self):
        for test in tests:
            got = longest_increasing_subsequence(test.xs)
            self.assertEqual(test.want, got, test)


if __name__ == '__main__':
    unittest.main()
