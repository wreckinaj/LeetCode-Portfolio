'''
Given an array of integers arr, return true if the number of occurrences of
each value in the array is unique or false otherwise.
'''

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Use a map to keep track of the frequencies of each number
        num_map = {}
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        # Use a set on the map's values and return False if there is a 'reduction',
        # meaning the frequencies are not unique
        return len(num_map) == len(set(num_map.values()))