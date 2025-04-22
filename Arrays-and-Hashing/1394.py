'''
Given an array of integers arr, a lucky integer is an integer that has a
frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer,
return -1.
'''

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # Use a map to keep track of the frequencies of each number
        num_map = {}
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        res = -1
        for num in num_map.keys():
            # Here we check if a number is a lucky integer and if it's
            # the largest (since the map is unordered)
            if num == num_map[num] and res < num:
                res = num
        return res