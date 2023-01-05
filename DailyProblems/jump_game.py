"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max = 0
        for current_step in range(len(nums)):
            if current_step > max:
                return False
            if current_step + nums[current_step] > max:
                max = current_step +nums[current_step]
        return True
test = Solution()
print(test.canJump([3,2,1,0,4]))