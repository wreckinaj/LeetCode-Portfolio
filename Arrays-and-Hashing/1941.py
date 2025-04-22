'''
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number
of occurrences (i.e., the same frequency).
'''

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # Use a map to keep track of the frequencies of each character
        c_map = {}
        for c in s:
            c_map[c] = c_map.get(c, 0) + 1
        # Here I am taking a random frequency to compare to
        freq = c_map[s[0]]
        for v in c_map.values():
            # Check if frequencies are equal, and if not, this is a bad string
            if v != freq:
                return False
        return True