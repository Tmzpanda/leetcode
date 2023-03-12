# 79. Word Search - if exists - dfs O(mn * 3^length)
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, {(i, j)}, word, 1):
                        return True
        return False
    
    
    def dfs(self, board, x, y, visited, word, index):
        if index == len(word):
            return True
        
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if not self.isValid(board, x_next, y_next, visited, word, index):
                continue
            
            visited.add((x_next, y_next))
            if self.dfs(board, x_next, y_next, visited, word, index + 1):
                return True
            visited.discard((x_next, y_next))
        
        return False
            
            
    def isValid(self, grid, i, j, visited, word, index):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        
        return grid[i][j] == word[index]
      