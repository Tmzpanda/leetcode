# 1091. Shortest Path in Binary Matrix - bfs
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        n = len(grid)
        start, end = (0, 0), (n - 1, n - 1)
        
        queue = deque([start])      
        visited = set()
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == end:
                    return level
                    
                for delta_x, delta_y in DIRECTIONS:
                    next_x = x + delta_x
                    next_y = y + delta_y
                    if not self.isValid(grid, next_x, next_y, visited):
                        continue
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    
        return -1
                    
    def isValid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False

        return not grid[i][j]
      