# 743. Network Delay Time

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:

    # build graph
    graph = defaultdict(list)
    for f, t, w in times:
        graph[f].append((t, w))

    # dijkstra
    min_heap = [(0, k)] # (distance_to_origin, current_node)
    visited = set()
    res = 0
    while min_heap:
        current_weight, current_node = heappop(min_heap)
        if current_node not in visited:     # 
            visited.add(current_node)
            res = max(res, current_weight)

        for next_node, next_weight in graph[current_node]:
            if next_node not in visited:
                heappush(min_heap, (current_weight + next_weight, next_node))

    return res if len(visited) == n else -1

