'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointers, one starting at index 0 and the other at -1
        l = 0
        r = len(s) - 1
        while l < r:
            # Only check left pointer if character is alphanumeric
            while l < r and not s[l].isalnum():
                l += 1
            # Same for right pointer
            while l < r and not s[r].isalnum():
                r -= 1
            # Check if characters mismatch (casing does not matter)
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True