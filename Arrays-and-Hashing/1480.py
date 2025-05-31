'''
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
'''

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        # The resulting array is a direct application of forming prefix sums
        for i in range(1, len(nums)):
            ans.append(ans[i - 1] + nums[i])
        return ans