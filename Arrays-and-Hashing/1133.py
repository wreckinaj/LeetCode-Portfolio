'''
Given an integer array nums, return the largest integer that only occurs
once. If no integer occurs once, return -1.
'''

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        # Use a map to count how many times an element appears
        num_map = {}
        # Loop through array to count each element
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        res = -1
        # Loop through map to find an element that appears only once. Store
        # if it's the largest number we find.
        for num in num_map:
            if num_map[num] == 1 and num > res:
                res = num
        return res