"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""
class Solution(object):
    def findLucky(self, arr):

        frequency = {}

        for num in arr:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1
        lucky_int = -1
        for num, count in frequency.items():
            if num == count and num > lucky_int:
                lucky_int = num

        return lucky_int


test = Solution()
print(test.findLucky([2,2,2,3,3]))