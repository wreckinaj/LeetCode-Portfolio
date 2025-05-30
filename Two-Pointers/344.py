'''
Write a function that reverses a string. The input string is given as an
array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Use two pointers, one for the leftmost character, and the other
        # for the rightmost character
        l, r = 0, len(s) - 1
        while l < r:
            # Since the input is a list, we can directly modify elements of it.
            # We simply need to swap the characters before moving inwards.
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1