# bfs
# https://www.youtube.com/watch?v=bD8RT0ub--0 黄浩杰 BFS和DFS 第2讲
from Graph import weighted_graph
from collections import defaultdict, deque
from heapq import heappush, heappop
from collections import deque

def bfs(graph, start):

    queue = deque([start])
    visited = set([start])
    res = []

    while queue:
        node = queue.popleft()

        for neighbor_node in graph[node]:
            if neighbor_node not in visited:
                queue.append(neighbor_node)
                visited.add(neighbor_node)

        res.append(node)

    return res


# dfs
# iteration
def dfs(graph, start):

    stack = [start]
    visited = set([start])
    res = []

    while stack:
        node = stack.pop()

        for neighbor_node in graph[node]:
            if neighbor_node not in visited:
                stack.append(neighbor_node)
                visited.add(neighbor_node)

        res.append(node)

    return res


# dfs
# recursion
# https://www.programiz.com/dsa/graph-dfs
def dfs(graph, start):

    def rec(graph, start, visited, res):
        visited.add(start)
        res.append(start)

        for neighbor_node in graph[start]:
            if neighbor_node not in visited:    # compare with n-ary tree - we don't need consider visited or not in tree, but needs to consider None or not
                rec(graph, neighbor_node, visited, res) 


    visited = set()
    res = []
    rec(graph, start, visited, res)

    return res


# all paths in a DAG
# https://leetcode.com/problems/all-paths-from-source-to-target/
def allPathsSourceTarget(graph, start, end):

    def dfs(graph, start, end, path, res):

        if start == end:
            res.append(list(path))
        
        for neighbor_node in graph[start]:
            path.append(neighbor_node)
            dfs(graph, neighbor_node, end, path, res)
            path.pop()

        return

    path = [start]
    res = []
    dfs(graph, start, end, path, res)
    return res


# shortest path
def shortest(graph, start, end):

    visited = set([start])
    previous_map = {start: None}  # previous_map for recording the path

    queue = deque([start])  
    while queue:
        vertex = queue.popleft()
        neighbors = graph[vertex]

        for node in neighbors:
            if node not in visited:
                queue.append(node)
                visited.add(node)
                previous_map[node] = vertex

    res = [end]
    while end:
        end = previous_map[end]
        res.append(end)

    return res


# dijkstra
# Find shortest path between start node and a arbitrary node in an weighted graph
# O(E*logV)
"""
https://www.youtube.com/watch?v=JLARzu7coEs Dijkstra 示例
https://www.youtube.com/watch?v=9wV1VxlfBlI 黄浩杰 BFS和DFS 第3讲 Dijkstra
"""
def dijkstra(graph, start):

    visited = set([start])
    previous_map = {start: None}  # {current_node: previous_node}
    # {current_node: distance_to_origin}
    distance_map = defaultdict(lambda: float('inf'))
    pqueue = [(0, start)]  # (distance_to_origin, current_node)

    while pqueue:
        current_distance, vertex = heappop(pqueue)
        visited.add(vertex)

        for neighbor_node in graph[vertex].keys():
            if neighbor_node not in visited:
                if current_distance + graph[vertex][neighbor_node] < distance_map[neighbor_node]:
                    heappush(pqueue, (current_distance +
                             graph[vertex][neighbor_node], neighbor_node))
                    previous_map[neighbor_node] = vertex
                    distance_map[neighbor_node] = current_distance + \
                        graph[vertex][neighbor_node]

    return distance_map, previous_map


# input
graph = weighted_graph
# output
distance_map, previous_map = dijkstra(graph, "A")
print(distance_map)
print(previous_map)



# bellman_ford
def bellman_ford(graph, start):
    """
    Find the shortest path from start node to all other nodes in a weighted graph using Bellman-Ford algorithm.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in graph:
        for v, weight in graph[u].items():
            if distances[u] + weight < distances[v]:
                raise ValueError("Negative weight cycle detected")

    return distances
