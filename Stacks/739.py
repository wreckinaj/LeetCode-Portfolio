'''
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Use a monotonic decreasing stack to keep track of the temperatures we have
        # yet to find a warmer temperature for
        stack = []
        # Make sure answer array entries are 0 by default
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            # We start popping elements off the stack when we find a warmer temperature
            while stack and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)
        return answer