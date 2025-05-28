'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        # Loop through all numbers in the list
        for num in nums:
            # Keep count of how many 1's we run into
            if num == 1:
                curr += 1
            # If we run into a 0, there are no more consecutive 1's, so we reset
            # the count and update ans if curr is at a peak.
            else:
                ans = max(ans, curr)
                curr = 0
        ans = max(ans, curr)
        return ans