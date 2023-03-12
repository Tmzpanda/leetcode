# 444. Sequence Reconstruction 
from functools import reduce
def sequenceReconstruction(org, seqs):
    
    # edge case  
    nodes = reduce(set.union, seqs, set())   # set.union(set([1, 2]), set([2, 3]))
    if nodes != set(org):                     
        return False

    n = len(org)
    out_edges = [[] for _ in range(n + 1)]
    in_degrees = [0 for _ in range(n + 1)]
    for seq in seqs:
        for f, t in zip(seq, seq[1:]):      
            out_edges[f].append(t)
            in_degrees[t] += 1

    queue = [node for node in org if in_degrees[node] == 0]
    order = []
    while queue:
        if len(queue) != 1:     # unique reconstruction
            return False
        node = queue.pop()
        order.append(node)
        for next_node in out_edges[node]:
            in_degrees[next_node] -= 1
            if not in_degrees[next_node]:
                queue.append(next_node)

    return org == order         # reconstruct
