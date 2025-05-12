'''
Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not 
use the same element twice.

Your solution must use only constant extra space.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # We use two pointers to find the two numbers that add up to the target
        # since the array is sorted
        l, r = 0, len(numbers) - 1
        while l < r:
            # Return the 1-based indices if the numbers add up to the target
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            # We increase the left pointer to increase the sum
            elif numbers[l] + numbers[r] < target:
                l += 1
            # We decrease the right pointer to decrease the sum
            else:
                r -= 1
        return []