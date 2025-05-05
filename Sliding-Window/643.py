'''
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average
value and return this value. Any answer with a calculation error less than 10-5 will
be accepted.
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        # Collect the average of the first subarray of length k
        for i in range(k):
            sum += nums[i]
        avg = sum / k
        # Slide the window by one in each iteration, and update the average.
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i - k]
            avg = max(avg, sum / k)
        return avg