"""
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.
"""
class Solution(object):
    def countLargestGroup(self, n):
        group_sizes = {}

        for i in range(1, n+1):
            digit_sum = sum([int(ch) for ch in str(i)])
            if digit_sum not in group_sizes:
                group_sizes[digit_sum] = 1
            else:
                group_sizes[digit_sum] += 1

        max_size = max(group_sizes.values())
        count = 0
        for size in group_sizes.values():
            if size == max_size:
                count += 1

        return count
test = Solution()
print(test.countLargestGroup(46))