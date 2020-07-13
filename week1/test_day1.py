import unittest
from day1 import *

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.solution1 = Solution2sum()
        self.solution2 = SolutionRevInteger()
        self.solution3 = SolutionPalindromeNum()
        self.solution4 = SolutionRomanInt()
        self.solution5 = SolutionPrefix()
        self.solution6 = SolutionBracket()

    def test_Solution2sum(self):
        self.assertEqual(self.solution1.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_SolutionRevInteger(self):
        self.assertEqual(self.solution2.reverse(-123), -321)
        self.assertEqual(self.solution2.reverse(120), 21)
        self.assertEqual(self.solution2.reverse(145), 541)

    def test_SolutionPalindromeNum(self):
        self.assertEqual(self.solution3.isPalindrome("racecar"), True)
        self.assertEqual(self.solution3.isPalindrome("level"), True)
        self.assertEqual(self.solution3.isPalindrome("james"), False)

    def test_SolutionRomanInt(self):
        self.assertEqual(self.solution4.romanToInt("VIII"), 8)
        self.assertEqual(self.solution4.romanToInt("IXXI"), 20)

    def test_SolutionPrefix(self):
        self.assertEqual(self.solution5.longestCommonPrefix(["flower", "florist", "fling"]), "fl")
        self.assertEqual(self.solution5.longestCommonPrefix(["james", "hongyao", "fangjing"]), "")

    def test_SolutionBracket(self):
        self.assertEqual(self.solution6.isValid("{}[]()"), True)
        self.assertEqual(self.solution6.isValid("{[{()}]}"), True)
        self.assertEqual(self.solution6.isValid("{([})]"), False)

if __name__ == '__main__':
    unittest.main()
