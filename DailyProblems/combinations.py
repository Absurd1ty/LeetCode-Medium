"""
Given two integers n and k, return all possible
combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""
class Solution(object):
    def combine(self, n, k):
        if k == 0:
            return [[]]
        else:
            comb = []
            for c in self.combine(n, k-1):
                for i in range(1, n+1):
                    if i not in c:
                        comb.append(c + [i])
            return comb

test = Solution()
print(test.combine(4, 2))

