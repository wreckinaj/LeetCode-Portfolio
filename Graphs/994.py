'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange
becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange. If this is impossible, return -1.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Helper function for determining if we staying inside the grid and
        # reaching a fresh orange
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        m, n = len(grid), len(grid[0])
        # Use a queue for BFS
        q = deque()
        # We want to keep track of how many fresh oranges are left
        countFresh = 0
        
        #Load initial rotten oranges and count fresh
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    countFresh += 1
        # If there are no fresh oranges, no further action is required
        if countFresh == 0:
            return 0
        # If there are no rotten oranges, the fresh oranges will never be rotten.
        if not q:
            return -1

        minutes = -1
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        # Perform the BFS simulation
        while q:
            # Use this loop so we only loop through the oranges that are already rotten
            # prior to the minute beginning
            for _ in range(len(q)):
                x, y = q.popleft()
                # Check all four directions
                for dx, dy in directions:
                    i, j = x + dx, y + dy
                    # If valid, the next orange becomes rotten, and we account for it
                    # in the next iteration
                    if valid(i,j):
                        grid[i][j] = 2
                        countFresh -= 1
                        q.append((i, j))
            minutes += 1

        # We have an answer only if there are no fresh oranges left.
        return minutes if countFresh == 0 else -1