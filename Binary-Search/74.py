'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Set up problem for binary search
        rows, cols = len(matrix), len(matrix[0])
        # The two variables represent the indices of matrix from 0 to n * m
        start, end = 0, rows * cols - 1
        while start <= end:
            # Prepare to cut matrix search window in half
            mid = (start + end) // 2
            # Get row and column values at the middle index
            row, col = mid // cols, mid % cols
            if target < matrix[row][col]:
                end = mid - 1
            elif target > matrix[row][col]:
                start = mid + 1
            else:
                return True
        return False