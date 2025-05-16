'''
Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        # Use this variable and change it to different powers of 2
        sub = 1
        for i in range(1, n + 1):
            # Change sub variable when we enter a new power of 2 range
            if sub * 2 == i:
                sub = i
            # The ith index depends on the value of the number with the same number of
            # 1s in their corresponding place values
            ans[i] = ans[i - sub] + 1 
        return ans