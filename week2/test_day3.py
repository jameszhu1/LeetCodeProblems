import unittest
from day3 import *


class TestDay3Solutions(unittest.TestCase):

    def setUp(self):
        self.q1 = StockSolution()
        self.q2 = Stock2Solution()
        self.q3 = SentencePalindromeSolution()

    def test_StockSolution(self):
        self.assertEqual(self.q1.maxProfit([7, 1, 5, 3, 6, 4]), 5)


    def test_Stock2Solution(self):
        self.assertEqual(self.q2.maxProfit([7, 1, 5, 3, 6, 4]), 7)

    def test_SentencePalindromeSolution(self):
        self.assertEqual(self.q3.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(self.q3.isPalindrome("race a car"), False)


if __name__ == '__main__':
    unittest.main()
