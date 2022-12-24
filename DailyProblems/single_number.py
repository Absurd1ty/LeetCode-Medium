"""
Given an integer array nums where every element appears three times except for one, which appears exactly once.
Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
class Solution(object):

    """
    Obvious solution but it uses constant extra space.


    def singleNumber(self, nums):
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] +=1
            else:
                num_count[num] = 1
        for num, count in num_count.items():
            if count == 1:
                return num
    """
    """
    O(nlogN) time complextity but good memory.
    I dont know solution for both linear time and costant memoery. 
    """

    def singleNumber(self, nums):
        nums.sort()
        for i in range (0, len(nums)-2, 3):
            if nums[i] != nums[i+1] or nums[i+1] != nums[i+2]:
                return nums[i]
        return nums[-1]


test = Solution()
print(test.singleNumber([0,1,0,1,0,1,99]))