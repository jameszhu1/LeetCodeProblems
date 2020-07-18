import unittest
from day5 import *

class test_day5Solutions(unittest.TestCase):

    def setUp(self):
        self.q1 = TwoSum2Solution()
        self.q2 = MajorityElementSolution()
        self.q3 = ZeroCountFactorialSolution()

    def test_twoSum2Solution(self):
        self.assertEqual(self.q1.twoSum([2,7,11,15], 9), [1,2])

    def test_majorityElementSolution(self):
        self.assertEqual(self.q2.majorityElement([3,2,3]), 3)
        self.assertEqual(self.q2.majorityElement([2,2,1,1,1,2,2]), 2)

    def test_ZeroCountFactorialSolution(self):
        self.assertEqual(self.q3.trailingZeroes(100), 24)

if __name__ == '__main__':
    unittest.main()
