'''
You are given a 0-indexed integer array nums of size 3 which can form the sides
of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.

Return a string representing the type of triangle that can be formed or "none"
if it cannot form a triangle.
'''

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # We form a triangle if all sides satisfy the triangle inequalities
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return 'none'
        # If side lengths are equal, the triangle is equilateral
        elif nums[0] == nums[1] == nums[2]:
            return 'equilateral'
        # If two side lengths match, the triangle is isosceles
        elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
            return 'isosceles'
        # If all side lengths differ, the triangle is scalene
        else:
            return 'scalene'