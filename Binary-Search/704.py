'''
Given an array of integers nums which is sorted in ascending order, and an integer
target, write a function to search target in nums. If target exists, then return its
index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Since the array is sorted, we use binary search to get the time
        # complexity we want. We start by using two pointers
        l, r = 0, len(nums) - 1
        # If the two pointers cross paths without finding a solution, then
        # there is no solution
        while l <= r:
            # Declare a middle variable to cut our window size in half each
            # iteration
            mid = (l + r) // 2
            # take away the right half because here elements there are too big
            if target < nums[mid]:
                r = mid - 1
            # take away the left half because here elements there are too small
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1