import unittest
from PalindromeNumber import palindrome_number 
import random

class TestPalindrom(unittest.TestCase):

    def solution(self, x):
        new_num = 0
        copy_num = x
        
        while(copy_num/10>0):
            new_num = (new_num*10) + copy_num %10
            copy_num = copy_num // 10
        
        return new_num == x


    def test_sum(self):
        for i in range(300000):
            num = random.randint(0,i)
            user = palindrome_number(num)
            actual = self.solution(num)
            self.assertEqual(user, actual, "For number "+str(num)+" expected "+str(actual)+" got "+str(user))

if __name__ == '__main__':
    unittest.main()
