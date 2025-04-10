'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''

# First solution:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # keep track of all numbers
        num_set = set(nums)
        # Loop through all numbers up to and including n
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
        return -1

# Improved solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # We get the range sum
        range_sum = (n * (n + 1)) // 2
        # We get the sum of all elements of nums
        nums_sum = sum(nums)
        # The difference between our two sums gives our missing number
        return range_sum - nums_sum