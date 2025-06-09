'''
You are given an array of integers nums, there is a sliding window of size k which
is moving from the very left of the array to the very right. You can only see the
k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # Use a deque to append elements as we expand the window, but pop from both
        # ends where needed. We need this to be monotonically decreasing.
        d = deque()
        for i in range(len(nums)):
            # We pop from the right end of the queue to pop the elements that are
            # smaller than the current element
            while d and nums[i] > nums[d[-1]]:
                d.pop()
            # Append the index of the current element
            d.append(i)
            # We pop from the left if our window is too large.
            if d[0] + k == i:
                d.popleft()
            # Only add to the window answer when our window is size k
            if i >= k - 1:
                ans.append(nums[d[0]])
        return ans