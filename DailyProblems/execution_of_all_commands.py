"""
There is an n x n grid, with the top-left cell at (0, 0) and the bottom-right cell at (n - 1, n - 1).
You are given the integer n and an integer array startPos where
startPos = [startrow, startcol] indicates that a robot is initially at cell (startrow, startcol).

You are also given a 0-indexed string s of length m where s[i] is the ith instruction for the robot: 'L'
(move left), 'R' (move right), 'U' (move up), and 'D' (move down).

The robot can begin executing from any ith instruction in s.
It executes the instructions one by one towards the end of s but it stops if either of these conditions is met:

The next instruction will move the robot off the grid.
There are no more instructions left to execute.
Return an array answer of length m where answer[i]
is the number of instructions the robot can execute if the robot begins executing from the ith instruction in s.
"""
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        answer = [0] * len(s)
        for i in range(len(s)):
            row = startPos[0]
            col = startPos[1]
            count = 0
            for j in range(i, len(s)):
                if s[j] == 'L' and col == 0:
                    break
                if s[j] == 'R' and col == n - 1:
                    break
                if s[j] == 'U' and row == 0:
                    break
                if s[j] == 'D' and row == n - 1:
                    break

                if s[j] == 'L':
                    col -= 1
                elif s[j] == 'R':
                    col += 1
                elif s[j] == 'U':
                    row -= 1
                elif s[j] == 'D':
                    row += 1
                count += 1
            answer[i] = count

        return answer

test = Solution()
print(test.executeInstructions(3, [0,1], "RRDDLU"))