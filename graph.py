"""Graph Algorithms."""

from heapq import heapify, heappush, heappop


INF = float("inf")


class PriorityQueue:
    def __init__(self, iterable):
        self.heap = iterable.copy()
        heapify(self.heap)

    def pop(self):
        return heappush(self.heap)

    def push(self, x):
        return heappush(self.heap, x)



