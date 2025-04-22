'''
You are given an integer array nums. The unique elements of an array are the
elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
'''

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Use a map to keep track of the frequency of each number
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        sum = 0
        for num in num_map.keys():
            # We only add the number in if it appears only once (hence unique)
            if num_map[num] == 1:
                sum += num
        return sum