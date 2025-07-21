'''
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to make
it fancy.

Return the final string after the deletion. It can be shown that the answer will
always be unique.
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        # Use a pointer to keep track of where we find the last "unique" character
        p = 0
        # Keep track of how many times we run into the character
        curr = 1
        # Need to start a new string since strings are immutable
        fancy_string = s[0]
        for i in range (1, len(s)):
            # Increment count if we run into consecutive characters
            if s[i] == s[p]:
                curr += 1
            # Here we reset the counter and track a new character
            else:
                curr = 1
                p = i
            # Do not append to string if we will end up with three (or more) in a row
            if curr > 2:
                continue
            fancy_string += s[i]
        return fancy_string