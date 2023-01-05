"""
An integer n is strictly palindromic if,
for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.

Given an integer n, return true if n is strictly palindromic and false otherwise.

A string is palindromic if it reads the same forward and backward.
"""
class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """

        def toBase(number, base):
            res = ""
            while number >= 1:
                res = str(number % base) + res
                number //= base
            return res

        for base in range(2, n-1):
            s = toBase(n,base)
            if s != s[::-1]:
                return False
        return True

test =Solution()
print(test.isStrictlyPalindromic(3))