import unittest
from TwoSum import two_sum

class TestSum(unittest.TestCase):

       
       

    def test_sum1(self):
        nums1 = [2,7,11,15]
        target1 = 9;
        found = True
        total = ""
        user = two_sum(nums1,target1)
        solve = [0,1]
        self.assertEqual(user, solve, "For input"+str(nums1)+"output should be"+str(solve))

    def test_sum2(self):
        nums2 = [3,2,4]
        target2 = 6;
        found = True
        total = ""
        user = two_sum(nums2,target2)
        solve = [1,2]
        self.assertEqual(user, solve, "For input"+str(nums2)+"output should be"+str(solve))

    def test_sum3(self):
        nums3 = [3,3]
        target3 = 6;
        found = True
        total = ""
        user = two_sum(nums3,target3)
        solve = [0,1]
        self.assertEqual(user, solve, "For input"+str(nums3)+"output should be"+str(solve))

    def test_sum4(self):
        nums4 = [2,7,11,15]
        target4 = 40;
        found = True
        total = ""
        user = two_sum(nums4,target4)
        solve = None
        self.assertEqual(user, solve, "For input"+str(nums4)+"output should be"+str(None))

    def test_sum5(self):
        nums5 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,24,25,26,27,28,29]
        target5 = 57
        found = True
        total = ""
        user = two_sum(nums5,target5)
        solve = [nums5.index(28),nums5.index(29)]
        self.assertEqual(user, solve, "For input"+str(nums5)+"output should be"+str(None))


    
if __name__ == '__main__':
    unittest.main()
