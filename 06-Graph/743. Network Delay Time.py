# 743. Network Delay Time
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:

    # build graph
    graph = defaultdict(list)
    for f, t, w in times:
        graph[f].append((t, w))

    # dijkstra
    min_heap = [(0, k)] 
    visited = set([k])
    while min_heap:
        weight, node = heappop(min_heap)
        visited.add(node)
        if len(visited) == n:
            return weight

        for next_node, next_weight in graph[node]:
            if next_node not in visited:
                heappush(min_heap, (weight + next_weight, next_node))

    return -1

