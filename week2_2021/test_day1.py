from day1 import *
import unittest




class TestDay1(unittest.TestCase):

    def setUp(self):
        self.solution1 = SolutionWaterContainer()
        self.solution2 = SolutionComboSum()




    def test_SolutionWaterContainer(self):
        self.assertEqual(self.solution1.maxArea([1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(self.solution1.maxArea([4,3,2,1,4]), 16)
        self.assertEqual(self.solution1.maxArea([1, 1]), 1)

    def test_SolutionComboSum(self):
        self.assertEqual(self.solution2.combinationSum([2,3,6,7], 7), [[2,2,3],[7]])
        self.assertEqual(self.solution2.combinationSum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])
        self.assertEqual(self.solution2.combinationSum([2], 1), [])

if __name__ == '__main__':
    unittest.main()
