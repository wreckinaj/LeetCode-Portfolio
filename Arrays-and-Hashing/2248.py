'''
Given a 2D integer array nums where nums[i] is a non-empty array of distinct
positive integers, return the list of integers that are present in each array of
nums sorted in ascending order.
'''

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # Make initial set of first array
        res = set(nums[0])
        for i in range(1, len(nums)):
            # Make a set of observed array and take the intersection
            res &= set(nums[i])
        # Convert set to a list
        res = list(res)
        res.sort()
        return res