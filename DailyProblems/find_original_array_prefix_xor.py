"""
You are given an integer array pref of size n.
Find and return the array arr of size n that satisfies:

pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i].
Note that ^ denotes the bitwise-xor operation.

It can be proven that the answer is unique.
"""
class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = [pref[0]] * len(pref)
        for i in range(1, len(arr)):
            arr[i] = pref[i] ^ pref[i-1]
        return arr

test = Solution()

print(test.findArray([5,2,0,3,1]))