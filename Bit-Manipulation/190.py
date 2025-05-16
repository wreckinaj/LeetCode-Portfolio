'''
Reverse bits of a given 32 bits unsigned integer.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        # Use to store result
        r = 0
        # Solution requires looping through n from right to left
        for _ in range(32):
            # Left shift answer variable (we add bits from left to right)
            r <<= 1
            # If n is odd, we turn the current rightmost bit of r to 1
            if (n & 1) == 1:
                r |= 1
            # Right shift n to move to the next bit at the left
            n >>= 1
        return r