"""
Given an integer array nums, find the
subarray
 which has the largest sum and return its sum.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(len(nums)-1):
            current_sum = max(current_sum + nums[i+1], nums[i+1])
            max_sum = max(current_sum, max_sum)
        return max_sum

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
