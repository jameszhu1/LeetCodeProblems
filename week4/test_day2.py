import unittest
from day2 import *

class TestDay2(unittest.TestCase):

    def setUp(self):
        self.q1 = MoveZeroesSolution()
        self.q2 = WordPatternSolution()
        self.q3 = NimSolution()
        self.q4 = PowerOfThreeSolution()
        self.q5 = ReverseStringSolution()

    def test_movezero(self):
        list1 = [0, 1, 0, 3]
        self.q1.moveZeroes(list1)
        self.assertEqual(list1, [1, 3, 0, 0])

        list2 = [10, 11, 12, 0, 0, 0]
        self.q1.moveZeroes(list2)
        self.assertEqual(list2, [10, 11, 12, 0, 0, 0])

    def test_wordPattern(self):
        self.assertTrue(self.q2.wordPattern("abba", "dog cat cat dog"))
        self.assertFalse(self.q2.wordPattern("abba", "dog cat cat fish"))
        self.assertTrue(self.q2.wordPattern("aaaa", "dog dog dog dog"))

    def test_NimGame(self):
        self.assertFalse(self.q3.canWinNim(4), False)
        self.assertFalse(self.q3.canWinNim(16), False)
        self.assertTrue(self.q3.canWinNim(5), True)
        self.assertTrue(self.q3.canWinNim(3), True)

    def test_powerOfThree(self):
        self.assertTrue(self.q4.isPowerOfThree(27), True)
        self.assertFalse(self.q4.isPowerOfThree(6), False)
        self.assertTrue(self.q4.isPowerOfThree(9), True)

    def test_reverseStr(self):
        s1 = ["h","e","l","l","o"]
        self.q5.reverseString(s1)
        self.assertEqual(s1, ["o","l","l","e","h"])

        s1 = ["j","a","m","e","s"]
        self.q5.reverseString(s1)
        self.assertEqual(s1, ["s","e","m","a","j"])

if __name__ == '__main__':
    unittest.main()
