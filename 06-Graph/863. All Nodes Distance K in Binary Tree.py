# 863. All Nodes Distance K in Binary Tree

# All nodes Distance K in a Binary Tree - O(m + n) = O(n-1 + n) = O(n)

def distanceK(root: TreeNode, target: TreeNode, K: int) -> List[int]:
  
    # build graph
    graph = defaultdict(list)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append(node.right)

    # bfs
    res = []
    queue = deque([(target, 0)])
    visited = set([target])
    while queue:
        node, distance = queue.popleft()
        if distance == K:
            res.append(node.val)

        else: 
            for next_node in graph[node]:
                if next_node not in visited:
                    queue.append((next_node, distance + 1))
                    visited.add(next_node)

    return res



