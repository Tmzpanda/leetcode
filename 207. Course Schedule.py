# 207. Course Schedule - one possible solution - bfs
from collections import deque

def findOrder(numCourses, prerequisites):
    out_edges = [[] for _ in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]
    for t, f in prerequisites:
        out_edges[f].append(t)
        in_degrees[t] += 1

    queue = deque([node for node in range(numCourses) if in_degrees[node] == 0])    # indegree
    order = []
    while queue:
        node = queue.popleft()      # not necessarily popoleft in topsort
        order.append(node)
        for next_node in out_edges[node]:
            in_degrees[next_node] -= 1
            if in_degrees[next_node] == 0:
                queue.append(next_node)

    if len(order) == numCourses:
        return order
    return []
