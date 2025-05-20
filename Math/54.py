'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Row variables
        i, m = 0, len(matrix) - 1
        # Column variables
        j, n = 0, len(matrix[0]) -1
        ans = []
        # Simulate the paths
        while i <= m and j <= n:
            # Traverse a row from the top boundary
            for k in range(j, n + 1):
                ans.append(matrix[i][k])
            i += 1
            # Traverse a column from the right boundary
            for k in range(i, m + 1):
                ans.append(matrix[k][n])
            n -= 1
            # Traverse a row from the bottom boundary
            if i <= m:
                for k in range(n, j - 1, -1):
                    ans.append(matrix[m][k])
                m -= 1
            # Traverse a column from the left boundary
            if j <= n:
                for k in range(m, i - 1, -1):
                    ans.append(matrix[k][j])
                j += 1
        return ans