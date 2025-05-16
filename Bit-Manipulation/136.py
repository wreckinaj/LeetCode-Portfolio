'''
Given a non-empty array of integers nums, every element appears twice except for
one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant
extra space.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # This will have our answer in the end.
        target = 0
        for num in nums:
            # The XOR operator will add in numbers provided in a sum formed throughout
            # this program, except when it runs into a number it already ran into,
            # in this case subtracts them, eventually giving the single number.
            target ^= num
        return target