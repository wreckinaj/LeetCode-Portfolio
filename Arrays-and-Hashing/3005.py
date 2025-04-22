'''
You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
'''
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # We store the maximum frequency
        max = 0
        # Use a map to keep track of the frequency of each map
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num,0) + 1
            # We change the max frequency when a element appears more than
            # the current value
            if num_map[num] > max:
                max = num_map[num]
        res = 0
        for num in num_map.keys():
            # Find elements with the max frequency, and if so, add that
            # max frequency in
            if num_map[num] == max:
                res += max
        return res