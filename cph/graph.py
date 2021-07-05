"""Graph Algorithms."""

from heapq import heapify, heappush, heappop


INF = float("inf")


class PriorityQueue:
    def __init__(self, iterable):
        self.heap = iterable.copy()
        heapify(self.heap)

    def pop(self):
        return heappop(self.heap)

    def push(self, x):
        heappush(self.heap, x)

    def __bool__(self):
        return len(self.heap) > 0


def dijkstra_dists(G, source):
    """Return the length of the shortest path from a starting node called source
    to other nodes in the graph G (assumed to be index from 0)."""
    distance = [INF for _ in range(len(G))]
    distance[source] = 0
    processed = {node: False for node in G}

    q = PriorityQueue([(0, source)])
    while q:
        a = q.pop()[1]
        if processed[a]:
            continue

        processed[a] = True
        for b, w in G[a]:
            if distance[a]+w < distance[b]:
                distance[b] = distance[a]+w
                q.push([-distance[b], b])

    return distance
