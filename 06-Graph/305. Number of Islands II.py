# 305. Number of Islands II - dynamic operatrion

def numIslands2(m: int, n: int, positions: List[List[int]]) -> List[int]:

    def union(a, b):
        a_root, b_root = find_root(a), find_root(b)
        if a_root == b_root:
            return False
        else:
            parent[a_root] = b_root
            return True

    def find_root(a):
        a_root = a
        while parent[a_root] != -1:
            a_root = parent[a_root]

        return a_root

    parent = defaultdict(lambda: -1)
    count = 0
    visited = set()
    res = []

    for i, j in positions:
        if (i, j) not in visited:
            visited.add((i, j))
            count += 1
            for delta in directions:
                x, y = i + delta[0], j + delta[1]
                if (x, y) in visited and union((i, j), (x, y)):
                    count -= 1
        res.append(count)
            
    return res




