'''
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the
last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.

Return the number of valid splits in nums.
'''

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Use a prefix sum to keep track of the sum of the first i + 1 elements
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])
        ans = 0
        for i in range(len(prefix) - 1):
            # The left section has a greater sum than the right section when the sum
            # up to prefix i are >= the difference of sums in the left and right
            # indices of the right section
            if prefix[i] >= prefix[-1] - prefix[i]:
                ans += 1
        return ans