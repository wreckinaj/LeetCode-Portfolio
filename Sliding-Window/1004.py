'''
Given a binary array nums and an integer k, return the maximum number of
consecutive 1's in the array if you can flip at most k 0's.
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        # Implement a sliding window and get the max window we can get where we flip
        # at most k zeros
        l = r = 0
        # Use a counter to keep track of how many zeros are in the list
        num_zeros = 0
        while r < len(nums):
            # Increment the counter when we run into a new 0
            if nums[r] == 0:
                num_zeros += 1
            # If we have more than k zeros, the window needs to be shrunk
            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            # Update answer with the length of the window
            ans = max(ans, r - l + 1)
            r += 1
        return ans