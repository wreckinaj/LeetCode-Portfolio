'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if a node is in the graph and is a 1 and should be added to the set
        def valid(row, col):
            return row >= 0 and row < m and col >= 0 and col < n and grid[row][col] == '1'

        # Perform DFS on the island to get all the nodes with a value of 1 in that
        # island without touching the water
        def dfs(row, col):
            # Perform DFS by checking all four possible directions
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                # If a node is valid, add to our set, and perform DFS on the next node
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        # Use a set to keep track of what 1 nodes we already came across
        seen = set()
        ans = 0
        m = len(grid)
        n = len(grid[0])
        # Easiest to loop through the entire graph
        for row in range(m):
            for col in range(n):
                # If a node is 1, we must use the set to see if we already checked the
                # node, and if we did, we came across an island we already explored,
                # and should not add an extra island. Otherwise, we found a new island
                # and must explore it with DFS!
                if grid[row][col] == '1' and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1
                    dfs(row, col)
        return ans