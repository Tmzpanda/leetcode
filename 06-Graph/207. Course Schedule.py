# 207. Course Schedule - if possible

def canFinish(numCourses, prerequisites):
    
    # build graph
    graph = [[] for _ in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]
    for t, f in prerequisites:
        graph[f].append(t)
        in_degrees[t] += 1

    # topological sort
    queue = [node for node in range(numCourses) if in_degrees[node] == 0] 
    order = []
    while queue:
        node = queue.pop()      # not necessarily popleft in topsort
        order.append(node)
        for next_node in graph[node]:
            in_degrees[next_node] -= 1
            if in_degrees[next_node] == 0:
                queue.append(next_node)

    return len(order) == numCourses
        
