'''
Given an array of integers nums and an integer k. A continuous subarray is called
nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
'''

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Keep track of the prefix sums
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        ans = 0
        # Keep track of the number of odd numbers
        prefix = 0
        for v in nums:
            # Update number of odd numbers by checking if v is odd
            prefix += v & 1
            # Is there a state where there are at least prefix - k odd numbers?
            if prefix - k >= 0:
                # Add the count of prefix sums up until this point for appropriate
                # counting of subarrays
                ans += cnt[prefix - k]
            # Increment count of current prefix sum
            cnt[prefix] += 1
        return ans