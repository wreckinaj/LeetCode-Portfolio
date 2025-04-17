'''
Given an integer array arr, count how many elements x there are, such that
x + 1 is also in arr. If there are duplicates in arr, count them separately.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        # Use a map so we can count each duplicate separately
        num_map = {}
        # Keep track of many times an element appears
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        res = 0
        # Loop through find the number of times we come across an element
        # n such that n + 1 exists
        for num in num_map:
            if (num + 1) in num_map.keys():
                res += num_map[num]
        return res