from day1 import *
import unittest



class TestDay1(unittest.TestCase):

    def setUp(self):
        self.solution1 = SolutionIntToRoman()
        self.solution2 = SolutionThreeSum()
        self.solution3 = SolutionGenerateParenthesis()


    def test_SolutionIntToRoman(self):
        self.assertEqual(self.solution1.intToRoman(48), "XLVIII")
        self.assertEqual(self.solution1.intToRoman(9), "IX")
        self.assertEqual(self.solution1.intToRoman(2048), "MMXLVIII")


    def test_SolutionThreeSum(self):
        self.assertEqual(self.solution2.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self.solution2.threeSum([]), [])
        self.assertEqual(self.solution2.threeSum([0]), [])

    def test_SolutionGenerateParenthesis(self):
        self.assertEqual(self.solution3.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])
        self.assertEqual(self.solution3.generateParenthesis(1), ["()"])


if __name__ == '__main__':
    unittest.main()
