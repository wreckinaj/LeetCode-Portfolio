'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two strings cannot be anagrams if they differ in length
        if len(s) != len(t):
            return False
        # Use a map to count the iterations of a character
        s_map = {}
        # Initialize or add one to the count of a character in s
        for c in s:
            s_map[c]=s_map.get(c,0) + 1
        # Check each character in t
        for c in t:
            # Not an anagram if there exists more of a certain character in t
            # or if a character exists in t but not in s. Note this handles the
            # case where there is less of a certain character in t because when
            # we previously check that their lengths are equal, there must exist
            # some extra character in t
            if c not in s_map or s_map[c] == 0:
                return False
            else:
                s_map[c] -= 1
        return True