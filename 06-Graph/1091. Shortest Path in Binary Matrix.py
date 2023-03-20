# 1091. Shortest Path in Binary Matrix 
# bfs
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    directions = [(-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]
    queue = deque([(0, 0, 1)])

    while queue:
        i, j, dist = queue.popleft()
        
        if i == n-1 and j == n-1:
            return dist
        
        for d in directions:
            x, y = i + d[0], j + d[1]
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                grid[x][y] = 1 
                queue.append((x, y, dist+1))

    return -1
