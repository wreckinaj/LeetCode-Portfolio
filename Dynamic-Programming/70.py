'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case 1: only one flight of stairs
        poss_1 = 1
        if n == 1:
            return poss_1
        # Base case 2: only two flights of stairs
        poss_2 = 2
        if n == 2:
            return poss_2
        # Keep track of last two possibilities, and add them together
        # Dummy variables are used for space complexity reduction
        for i in range(2, n):
            if poss_1 < poss_2:
                poss_1 = poss_1 + poss_2
            else:
                poss_2 = poss_1 + poss_2
        return max(poss_1, poss_2)