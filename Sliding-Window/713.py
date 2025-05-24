'''
Given an array of integers nums and an integer k, return the number of contiguous
subarrays where the product of all the elements in the subarray is strictly less
than k.
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Since all elements are positive, a product can never be strictly
        # less than 1
        if k <= 1:
            return 0
        # Use a sliding window approach, as we can get a longest possible subarray
        # in some spot, and then the subarrays of that subarray will also have
        # a product less than k
        ans = 0
        left = 0
        curr = 1
        for right in range(len(nums)):
            # Get the current product of the subarray
            curr *= nums[right]
            # We need to decrease the product if too large, so we increment the left
            # pointer
            while curr >= k:
                curr //= nums[left]
                left += 1
            # Add in the valid subarrays we found
            ans += right - left + 1
        return ans