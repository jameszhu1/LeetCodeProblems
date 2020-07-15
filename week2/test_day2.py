import unittest
from day2 import *

class testDay2Week2(unittest.TestCase):
    def setUp(self):
        self.question1 = PascalSolution()
        self.question2 = PascalRowSolution()

    def test_PascalSolution(self):
        self.assertEqual(self.question1.generate(5), [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
    def test_PascalRowSolution(self):
        self.assertEqual(self.question2.getRow(3), [1,3,3,1])

if __name__ == '__main__':
    unittest.main()
