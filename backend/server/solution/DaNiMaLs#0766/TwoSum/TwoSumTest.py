import unittest
from TwoSum import two_sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(two_sum([2,7,11,15],9),[0,1] , "Should be [0,1]")
        self.assertEqual(two_sum([3,2,4],6), [1,2], "Should be [1,2]")
        self.assertEqual(two_sum([3,3],6), [0,1], "Sould be [0,1]")


if __name__ == '__main__':
    unittest.main()
