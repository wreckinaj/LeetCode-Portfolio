'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Use a map to keep track of frequencies of each number
        num_map = {}
        for num in nums:
            num_map[num] = num_map.get(num, 0) + 1
        res = 0
        '''
        We can use the combinations formula for our solution. To use this correctly,
        we note we want to take 2 elements from a set. Then for a set with n elements,
        the number of possible combinations is n!/(2!(n-2)!)=(n(n-1))/2. Here, we let
        n be the frequency of the number taken, and we get a good pair by choosing 2
        indices where this number occurs. We add up the combinations to our counter.
        '''
        for num in num_map.keys():
            res += (num_map[num] * (num_map[num] - 1) // 2)
        return res