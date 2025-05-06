'''
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a map to keep track of the frequency of each element
        num_map = {}
        # We convert to a list later
        freq =[[] for i in range(len(nums) + 1)]
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        for num, cnt in num_map.items():
            freq[cnt].append(num)
        res = []
        # Traverse through the list backwards in order to get the top k elements
        for i in range(len(freq) - 1, -1, -1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
            if len(res) == k:
                return res
        return res