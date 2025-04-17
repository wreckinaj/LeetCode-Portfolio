'''
Given an integer array arr, count how many elements x there are, such that
x + 1 is also in arr. If there are duplicates in arr, count them separately.
'''

class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_map = {}
        for num in arr:
            num_map[num] = num_map.get(num, 0) + 1
        res = 0
        for num in num_map:
            if (num + 1) in num_map.keys():
                res += num_map[num]
        return res