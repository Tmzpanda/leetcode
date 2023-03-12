# 329. Longest Increasing Subarray - 2d - dfs memoization
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        record = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                record[i][j] = self.dfs(matrix, i, j, memo)
                
        return max(map(max, record))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if self.isValid(matrix, x_next, y_next) and matrix[x][y] < matrix[x_next][y_next]:
                longest = max(longest, self.dfs(matrix, x_next, y_next, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])