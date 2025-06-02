'''
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius
k is the average of all elements in nums between the indices i - k and i + k
(inclusive). If there are less than k elements before or after the index i, then
the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for
the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer
division. The integer division truncates toward zero, which means losing its
fractional part.

For example, the average of four elements 2, 3, 1, and 5 is
(2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
'''

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # No k-radius average can be formed if we cannot get the correct window size,
        # so we would just have -1 across the entire answer
        if len(nums) < 2 * k + 1:
            return [-1] * len(nums)
        # Use a prefix sum to keep track of the sum as we traverse the array
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        ans = [-1] * len(nums)
        for i in range(k, len(nums) - k):
            # The k-radius sum is the sum from the element k elements to the right
            # minus the sum from k elements to the left. Then we just divide by
            # our window size to get the average
            ans[i] = (prefix_sum[i + k + 1] - prefix_sum[i - k]) // (2 * k + 1)
        return ans