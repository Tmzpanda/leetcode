# 444. Sequence Reconstruction 

def sequenceReconstruction(nums: List[int], sequences: List[List[int]]) -> bool:
    
    # edge case  
    if set(reduce(lambda x, y: x + y, sequences)) != set(nums):         
        return False

    # build graph
    n = len(nums)
    graph = defaultdict(list)
    in_degrees = defaultdict(int)

    for seq in sequences:
        for f, t in zip(seq, seq[1:]):  
            graph[f].append(t)
            in_degrees[t] += 1

    # topological sort
    queue = [node for node in nums if in_degrees[node] == 0]
    order = []
    while queue:
        if len(queue) != 1:     # unique reconstruction
            return False
        node = queue.pop()
        order.append(node)
        for next_node in graph[node]:
            in_degrees[next_node] -= 1
            if not in_degrees[next_node]:
                queue.append(next_node)

    return nums == order        # reconstruct
