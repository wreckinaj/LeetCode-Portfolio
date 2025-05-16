'''
You are part of a university admissions office and need to keep track of the kth
highest test score from applicants in real-time. This helps to determine cut-off
marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream
of test scores and continuously returns the kth highest test score after a new score
has been submitted. More specifically, we are looking for the kth highest score in
the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream
of test scores nums.

int add(int val) Adds a new test score val to the stream and returns the element
representing the kth largest element in the pool of test scores so far.
'''

import heapq

class KthLargest:

    # Store the value of k, and initialize a priority queue object
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = []
        for num in nums:
            self.add(num)

    # Add in new student data and return the specified value
    def add(self, val: int) -> int:
        # Add new student if there is not enough data
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        # Here is where cutoffs happen
        elif val > self.pq[0]:
            heapq.heapreplace(self.pq, val)
        return self.pq[0]