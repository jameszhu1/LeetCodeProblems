import unittest
from day1 import *

class Test_day1(unittest.TestCase):
    def setUp(self):
        self.q1 = HappySolution()
        self.q3 = CountPrimesSolution()
        self.q4 = IsomorphicSolution()

    def test_happy(self):
        self.assertEqual(self.q1.isHappy(19), True)
        self.assertEqual(self.q1.isHappy(12), False)

    def test_countPrimes(self):
        self.assertEqual(self.q3.countPrimes(10), 4)

    def test_isomorphic(self):
        self.assertEqual(self.q4.isIsomorphic("egg", "add"), True)
        self.assertEqual(self.q4.isIsomorphic("foo", "bar"), False)
        self.assertEqual(self.q4.isIsomorphic("paper", "title"), True)

if __name__ == '__main__':
    unittest.main()
