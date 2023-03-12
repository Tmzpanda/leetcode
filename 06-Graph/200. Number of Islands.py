        
# 200. Number of Islands - bfs
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isValid(grid, i, j, visited):
                    self.bfs(grid, i, j, visited)
                    res += 1
                    
        return res                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.isValid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
    
    def isValid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
          
        return int(grid[i][j])
      
      
# dfs
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if self.isValid(grid, i, j, visited):         
                    visited.add((i, j))
                    self.dfs(grid, i, j, visited)
                    ans += 1

        return ans


    def dfs(self, grid, i, j, visited):
        for delta_i, delta_j in DIRECTIONS:
            i_next, j_next = i + delta_i, j + delta_j
            
            if not self.isValid(grid, i_next, j_next, visited):
                continue
                
            visited.add((i_next, j_next))
            self.dfs(grid, i_next, j_next, visited)     # no backtrack

    
    def isValid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        
        return int(grid[i][j])
