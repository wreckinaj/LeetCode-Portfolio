'''
You are given an array of integers stones where stones[i] is the weight of the
ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two
stones and smash them together. Suppose the heaviest two stones have weights x and
y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new
weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.
'''

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        # Use a heap to sort elements in order (since we want to take the max
        # stones each turn)
        heapq.heapify(h)
        # Multiply elements by -1 to turn into a max heap
        for stone in stones:
            heapq.heappush(h, -stone)
        while len(h) > 1:
            # Start of turn: pop two stones
            stone1, stone2 = heapq.heappop(h), heapq.heappop(h)
            # Add new difference stone where necessary
            if stone1 != stone2:
                heapq.heappush(h, -abs(stone2 - stone1))
        # Handle case of 1 stone left
        if len(h) == 1:
            return -heapq.heappop(h)
        # Case of 0 stones left
        else:
            return 0