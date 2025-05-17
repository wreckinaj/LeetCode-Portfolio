'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # easier to implement solution with a sorted list (does not contribute to
        # time complexity)
        nums.sort()
        ans = []
        # The method used is to loop through the entire list with one pointer for
        # reference
        for i, v in enumerate(nums):
            # To reduce time, we stop when we get to positive numbers, as numbers
            # from then on will never add up to zero
            if v > 0:
                break
            # Keep incremented i as necessary to avoid repeated steps and
            # duplicate entires to answer
            if i > 0 and v == nums[i - 1]:
                continue
            # Use two pointers on the rest of the array
            l, r = i + 1, len(nums) - 1
            while l < r:
                # Get the sum, and perform necessary logic
                trip_sum = v + nums[l] + nums[r]
                if trip_sum == 0:
                    # Append to list if sum adds up to zero
                    ans.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Increment left pointer to avoid duplicate entries
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                # The sum is too small, so we move to a larger entry
                elif trip_sum < 0:
                    l += 1
                # The sum is too large, so we move to a smaller entry
                else:
                    r -= 1
        return ans