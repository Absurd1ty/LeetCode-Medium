"""
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.
"""
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
            return False

        return True

test = Solution()
print(test.isBoomerang([[1,1],[2,3],[3,2]]))