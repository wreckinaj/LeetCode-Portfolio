'''
You are given an integer array cost where cost[i] is the cost of ith step on a
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # Using a memoization process
        costs = []
        for i in range(len(cost)):
            # The min cost to reach the first step is the cost at the first step
            if i == 0:
                costs.append(cost[0])
            # The min cost to reach the second step is the cost at the second step
            elif i == 1:
                costs.append(cost[1])
            # Since you only move up one or two steps each turn, you take the cost of
            # the current step plus the minimum cost from the last two steps
            else:
                costs.append(cost[i] + min(costs[i - 1], costs[i - 2]))
        return min(costs[n - 1], costs[n - 2])