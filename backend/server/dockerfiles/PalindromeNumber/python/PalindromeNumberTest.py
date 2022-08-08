import unittest
from PalindromeNumber import palindrome_number 
import random

class TestPalindrom(unittest.TestCase):

    def solution(self, x):
        return str(x)[::-1] == str(x)


    def test_sum(self):
        for i in range(30000):
            num = random.randint(0,i)
            user = palindrome_number(num)
            actual = self.solution(num)
            self.assertEqual(user, actual, "For number "+str(num)+" expected "+str(actual)+" got "+str(user))

if __name__ == '__main__':
    unittest.main()
