"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""
"""
I worked on a few solutions untill noticed the basic logic of the problem 
the amount of numbers wwe need to add is just the biggest digit in the number since we obviously will just replace 1s with 0 if we dont need anymore adding up
"""

class Solution:
    def minPartitions(self, n):
        return int(max(n))

test = Solution()
print(test.minPartitions("882734"))