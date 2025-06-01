'''
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in
nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is
never less than 1.
'''

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Use a prefix to keep track of the current sum as we traverse through the list
        prefix = 0
        # We want to keep track of the minimum prefix sum we get
        mini = float('inf')
        for num in nums:
            prefix += num
            mini = min(mini, prefix)
        # If the minimum prefix sum is positive, then any positive start value can
        # be adjusted and never fall below 0, so we return 1
        if mini > 0:
            return 1
        # Otherwise, -1 * mini will eventually see a prefix sum of 0, so we add 1
        # to it
        else:
            return -1 * mini + 1
        