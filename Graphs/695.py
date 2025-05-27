'''
You are given an m x n binary matrix grid. An island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.) You
may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        # Perform DFS on the graph
        def dfs(i, j):
            # Only look through the node if in the graph and the node is a land node
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            # Alter the node so we do not search through it again
            grid[i][j] = 0
            # The area of the island will be determined by the current node plus
            # the DFS results in each of the four directions
            return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
        # Loop through the entire graph
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    # Update answer to achieve the maximum area
                    res = max(res, dfs(i, j))
        return res