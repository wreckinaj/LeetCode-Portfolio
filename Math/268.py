'''
Given an array nums containing n distinct numbers in the range [0, n], return the
only number in the range that is missing from the array.
'''

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n, the maximum number possible, is the length of the list
        n = len(nums)
        # Use the summation formula to get the value of all numbers from 0 to n
        # added up
        range_sum = (n * (n + 1)) // 2
        # Get the value of all numbers in nums added up
        nums_sum = sum(nums)
        # The two values have the same numbers adding up to it except for one.
        # That is the answer.
        return range_sum - nums_sum