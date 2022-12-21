"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""
class Solution(object):
    def lengthofLongestSubstring(self, s):
        """
       :type s: str
       :rtype: int
       """
        used = {}
        maxlength = 0
        start = 0
        for idx, character in enumerate(s):
            if character in used and start <= used[character]:
                start = used[character] +1
            else:
                maxlength = max(maxlength, idx- start + 1)
            used[character] = idx

        return maxlength


test = Solution()
print(test.lengthofLongestSubstring("abcabcbbb"))