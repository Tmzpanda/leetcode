# 787. Cheapest Flights Within K Stops

# Dijkstra
def findCheapestPrice(n: int, flights, src: int, dst: int, k: int) -> int:

    # build graph
    graph = defaultdict(list)
    for f, t, w in flights:
        graph[f].append((t, w))

    # dijkstra
    min_heap = [(0, src, k+1)] 
    while min_heap:
        weight, node, stops_left = heappop(min_heap)
        if node == dst:
            return weight

        if stops_left > 0:
            for next_node, next_weight in graph[node]:      # directed graph
                heappush(min_heap, (weight + next_weight, next_node, stops_left-1))

    return -1


# Bellman-Ford
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

    prices = [sys.maxsize] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp_prices = list(prices)
        for  f, t, w in flights:
            if prices[f] + w < temp_prices[t]:
                temp_prices[t] = prices[f] + w

        prices = temp_prices

    return prices[dst] if prices[dst] != sys.maxsize else -1 
