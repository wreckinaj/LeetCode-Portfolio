'''
You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between
the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.

Return this maximum difference.
'''

class Solution:
    def maxDifference(self, s: str) -> int:
        # Use a hash map to count the frequency of each element
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        # The element at a_1 must be odd and a maximum, while the element at a_2 must
        # be even and a minimum. We loop through the values to get this minimum
        # and maximum before taking the difference
        max_odd, min_even = 0, float('inf')
        for v in char_map.values():
            if v % 2 == 0:
                min_even = min(min_even, v)
            else:
                max_odd = max(max_odd, v)
        return max_odd - min_even