'''
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Define a set to keep track of what numbers are in nums
        num_set = set(nums)
        # Since a set only contains one iteration of a single element,
        # there is a duplicate in nums if the lengths differ.
        if len(num_set) < len(nums):
            return True
        else:
            return False