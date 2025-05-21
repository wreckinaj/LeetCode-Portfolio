'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and
column to 0's.

You must do it in place.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # Use two arrays to store which rows and columns have zeros
        row, col = [0] * m, [0] * n
        # Loop through matrix to determine which elements have zeros
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] == 0):
                    row[i] = 1
                    col[j] = 1
        # Loop through matrix again. If there is a 0 in the row or column,
        # set the element to 0
        for i in range(m):
            for j in range(n):
                if(row[i] or col[j]):
                    matrix[i][j] = 0