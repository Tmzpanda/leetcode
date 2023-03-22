        
# 200. Number of Islands 

def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    res = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1" and (i, j) not in visited:
                res += 1
                bfs(grid, i, j, visited)        # bfs or dfs

    return res      


# bfs
def bfs(grid, i, j, visited):
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    queue = deque([(i, j)])
    visited.add((i, j))
    while queue:
        i, j = queue.popleft()
        for delta in directions:
            x, y = i + delta[0], j + delta[1]
            if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == "1":
                visited.add((x, y))
                queue.append((x, y))
                

      
# dfs
def dfs(grid, i, j, visited):
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    visited.add((i, j))
    for delta in directions:
        x, y = i + delta[0], j + delta[1]
        if 0 <= x < m and 0 <= y < n and (x, y) not in visited and grid[x][y] == "1":
            visited.add((x, y))
            dfs(grid, x, y, visited)
        
