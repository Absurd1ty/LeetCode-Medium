"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        num_vertices = len(graph)
        paths = []

        def dfs(current_vertex, path):
            if current_vertex == num_vertices - 1:
                paths.append(path)
            for neighbor in graph[current_vertex]:
                dfs(neighbor, path+[neighbor])

        dfs(0, [0])
        return paths
test = Solution()
print(test.allPathsSourceTarget([[1,2],[3],[3],[]]))