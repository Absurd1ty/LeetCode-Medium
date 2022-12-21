"""
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triplets = []
        nums.sort()
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left + 1
            right = len(nums)-1
            while mid < right:
                sum = nums[left] = nums[right] + nums[mid]
                if sum < 0:
                    mid +=1
                elif sum > 0:
                    right -=1
                else:
                    triplets.append(nums[left], nums[mid], nums[right])



