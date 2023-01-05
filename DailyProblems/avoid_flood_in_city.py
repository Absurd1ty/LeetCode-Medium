"""
Your country has an infinite number of lakes.
Initially, all the lakes are empty, but when it rains over the nth lake,
the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes
"""
class Solution:
    def avoidFlood(self, rains):
        result = []
        full_lakes = set()
        next_day = {}
        available_lakes = set ()

        for i, lake in enumerate (rains):
            if lake > 0:
                if lake in full_lakes:
                    return []
            full_lakes.add(lake)
            result.append(-1)
            next_day[lake] = i +1
            available_lakes.add(lake)
        else:
            if available_lakes:
                lake = available_lakes.pop()
                result.append(lake)
                full_lakes.remove(lake)
                next_day[lake] = 0
            else:
                result.append(1)
        return result
test = Solution()
print(test.avoidFlood([1,2,0,0,2,1]))