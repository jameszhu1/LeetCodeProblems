import unittest
from day1 import *

class Test_day1Solutions(unittest.TestCase):
    def setUp(self):
        self.q3 = DigitalRootSolution()
        self.q4 = MissingNumSolution()

    def test_badVersion(self):
        self.assertEqual(self.q3.addDigits(38), 2)

    def test_missingNum(self):
        self.assertEqual(self.q4.missingNumber([1, 0, 3]), 2)
        self.assertEqual(self.q4.missingNumber([1, 0, 3, 2, 5, 4]), 6)

if __name__ == '__main__':
    unittest.main()
