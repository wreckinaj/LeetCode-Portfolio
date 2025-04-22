'''
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a
type of stone you have. You want to know how many of the stones you have are
also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Use a set to collect what jewels we have for easier access
        jewel_set = set(jewels)
        res = 0
        # Loop through each stone to see which stones match a jewel
        for s in stones:
            if s in jewel_set:
                res += 1
        return res