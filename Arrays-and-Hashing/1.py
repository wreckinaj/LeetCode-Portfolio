'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use a map to store the indices of where each element exists
        num_map = {}
        for i in range (len(nums)):
            # We collect the number, and see if the difference required is
            # in our map
            diff = target - nums[i]
            if diff in num_map:
                return [i, num_map[diff]]
            # Store the index value of the number
            num_map[nums[i]] = i
        return []