'''
Given a string s consisting of lowercase English letters, return the first letter to appear twice.
'''

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # Use a set to keep track of what characters we have seen
        seen = set()
        # We go in order to find the first character
        for c in s:
            # The first character in our set we catch is our answer
            if c in seen:
                return c
            # Otherwise store for later
            else:
                seen.add(c)
        return ''