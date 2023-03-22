# 1091. Shortest Path in Binary Matrix 

# bfs
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    directions = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])
    while queue:
        i, j, distance = queue.popleft()
        if i == n - 1 and j == n - 1:
            return distance
        
        for delta in directions:
            x, y = i + delta[0], j + delta[1]
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited and grid[x][y] == 0:
                queue.append((x, y, distance + 1))
                visited.add((x, y))
                
    return -1
