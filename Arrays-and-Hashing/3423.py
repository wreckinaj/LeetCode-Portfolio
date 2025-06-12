'''
Given a circular array nums, find the maximum absolute difference between
adjacent elements.

Note: In a circular array, the first and last elements are adjacent.
'''

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = 0
        for i in range(len(nums)):
            # Handle edge case with first and last elements
            if i == 0:
                diff = max(diff, abs(nums[0] - nums[-1]))
            # Handle all other cases
            else:
                diff = max(diff, abs(nums[i] - nums[i - 1]))
        return diff