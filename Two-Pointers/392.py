'''
Given two strings s and t, return true if s is a subsequence of t, or false 
otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" 
while "aec" is not).
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use two pointers. The left pointer watches the smaller string s, while
        # the right pointer watches the larger string t
        l, r = 0, 0
        # Use two bounds to prevent overflow
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1
        # All characters of s must be traversed in order
        return l == len(s)