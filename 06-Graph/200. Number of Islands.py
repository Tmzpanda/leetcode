        
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
def bfs(self, grid, i, j, visited):
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    queue = deque([(i, j)])
    visited.add((i, j))
    while queue:
        i, j = queue.popleft()
        for delta in DIRECTIONS:
            x = i + delta[0]
            y = j + delta[1]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))

      
# dfs
def dfs(grid, i, j, visited):
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    visited.add((i, j))
    for delta in directions:
        x = i + delta[0]
        y = j + delta[1]
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1" and (x, y) not in visited:
            visited.add((x, y))
            dfs(grid, x, y, visited)
        
