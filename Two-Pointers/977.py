'''
Given an integer array nums sorted in non-decreasing order, return an
array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # We use this to store our sorted list
        ans = [0] * n
        # We use two pointers, one for the leftmost number, and the other
        # for the rightmost number
        l, r = 0, n - 1
        # We iterate backwards to ensure the squares of the larger elements will
        # always be towards the back of the sorted array
        for i in range(n - 1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                ans[i] = nums[l] ** 2
                l += 1
            else:
                ans[i] = nums[r] ** 2
                r -= 1
        return ans