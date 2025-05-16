'''
Given a positive integer n, write a function that returns the number of set bits
in its binary representation (also known as the Hamming weight).
'''

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # For loop because there are a maximum of 32 bits
        for i in range(32):
            # Perform a right shift of n by 1, and see if a 1 in the binary
            # representation is taken out
            if (n >> i) & 1:
                res += 1
            # Terminate early to avoid over repetition
            if n == 0:
                break
        return res