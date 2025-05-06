'''
You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Use the default value for which no profit can be obtained
        res = 0
        # The strategy is to buy at a low price, and then sell at a
        # higher cost later, so we keep track of the lowest price
        lowest = prices[0]
        for i in range(1, len(prices)):
            # Update the lowest price as needed
            lowest = min(lowest, prices[i])
            # We update the max if we can find a profit that is greater
            res = max(res, prices[i] - lowest)
        return res