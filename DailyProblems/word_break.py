"""
Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.


"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        checking_array = [False] * (length +1)
        checking_array[0] = True

        for start in range (length):
            for end in range(start +1, length+1):
                if checking_array[start] and s[start:end] in wordDict:
                    checking_array[end] = True
            print(checking_array)
        return checking_array[-1]


test = Solution()
print(test.wordBreak(("catsandog"),  ["cats","dog","sand","and","cat"]))