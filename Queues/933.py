'''
You have a RecentCounter class which counts the number of recent requests
within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.

int ping(int t) Adds a new request at time t, where t represents some time
in milliseconds, and returns the number of requests that has happened in the past
3000 milliseconds (including the new request). Specifically, return the number of
requests that have happened in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than
the previous call.
'''

class RecentCounter:

    def __init__(self):
        # Use the final note. If we use a queue, then we will always follow an
        # increasing order
        self.queue = deque()

    def ping(self, t: int) -> int:
        # Only keep items in the queue that have a value of t - 3000.
        # We make this easy by popping the front element.
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # Add the new request
        self.queue.append(t)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)