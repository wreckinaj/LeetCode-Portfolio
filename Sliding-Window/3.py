'''
Given a string s, find the length of the longest substring without duplicate
characters.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Implement a sliding window approach for checking the substrings
        l = 0
        ans = 0
        # Use a set to keep track of what characters we found already
        chars = set()
        for r in range(len(s)):
            # If a character is already in the set, then the current substring is
            # invalid, and we must remove the first instance of that repeated
            # character
            if s[r] in chars:
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1
            # Add new character to the set
            chars.add(s[r])
            # Update the maximum window size where needed
            ans = max(ans, r - l + 1)
        return ans