"""
# directed matrix
# Spiral Matrix - O(m*n)
# Maximal Sqaure - dp O(m*n)


# undirected matrix
# Number of Islands - bfs - O(m*n)
# Word Search - dfs T << O(m*n * 3^len(word))
# Longest Increasing Subarray 2d - dfs memoization - 



# chessboard
# Unique Paths - dp O(m*n)
# Knight Probability in Chessboard - dp O(K*n^2)
# Queens

"""

#************************************************** Directed Matrix ***********************************************************
# Spiral Matrix
"""
4x4
           l1
           ^
        t  t  t  t
   b2 > l  t  t  r  < t1
   b1 > l  b  r  r  < t2
        b  b  b  r
           ^  ^
           r2 r1


3x4
           l1
           ^
        t  t  t  t
   b1 > l  t  t  r  < t1
        b  b  b  r  < t2
              ^
              r1
"""
def spiralOrder(matrix):
    if not matrix: 
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    size = len(matrix) * len(matrix[0])
    result = []

    while len(result) < size:       # n*n
        for i in range(left, right + 1):
            if len(result) < size:          # m*n
                result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            if len(result) < size:
                result.append(matrix[i][right])
        right -= 1

        for i in range(right, left - 1, -1):
            if len(result) < size:
                result.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            if len(result) < size:
                result.append(matrix[i][left])
        left += 1
            
    return result



# Maximal Sqaure - dp O(m*n)
"""

1 1 1          
1 x = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
1 

"""
def maximalSquare(matrix):
    if not matrix: 
        return 0
    
    m , n = len(matrix), len(matrix[0])
    dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
    res = max(max(row) for row in dp)
    return res ** 2 



#************************************************** Undirected Matrix ***********************************************************

# Number of Islands
# bfs
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
from collections import deque
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, i, j, visited):
        queue = deque([(i, j)])
        visited.add((i, j))
        while queue:
            i, j = queue.popleft()
            for delta_i, delta_j in DIRECTIONS:
                next_i = i + delta_i
                next_j = j + delta_j
                if not self.is_valid(grid, next_i, next_j, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

           
    def is_valid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        return grid[i][j]


# Word Search - dfs
# T << O(m*n * 3^len(word))
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
            
            visited.add((x_next, y_next))        # backtrack
            if self.dfs(board, x_next, y_next, visited, word, index + 1):
                return True
            visited.remove((x_next, y_next))
        
        return False
            
            
    def isValid(self, grid, i, j, visited, word, index):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        return grid[i][j] == word[index]
        
           
          
# Longest Increasing Subarray 2d
# dfs memoization
"""
        0 1 2 3 4..... n
      0     #
      1   # x #
      2     #
      3      
      4
      .
      .
      m
""" 
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = self.dfs(matrix, i, j,  memo)
                
        return max(map(max, dp))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_prev, y_prev = x - delta_x, y - delta_y
            if not self.isValid(matrix, x_prev, y_prev) or matrix[x][y] <= matrix[x_prev][y_prev]:
                continue
            longest = max(longest, self.dfs(matrix, x_prev, y_prev, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
      
      
#**************************************************** Chessboard ********************************************************************
# Unique Paths O(m*n)
def uniquePaths(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
    return dp[m][n]


# Knight Probability in Chessboard - O(K*n^2)
DIRECTIONS = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), 
               (1, -2), (2, -1), (2, 1), (1, 2)]
               
class Solution:
    def knightProbability(self, N, K, r, c):
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
    
        for step in range(K):
            dpTemp = [[0 for i in range(N)] for j in range(N)]    
            for i in range(N):
                for j in range(N):
                    for direction in DIRECTIONS:
                        prev_i, prev_j = i - direction[0], j - direction[1]
                        if 0 <= prev_i < N and 0 <= prev_j < N:
                            dpTemp[i][j] += dp[prev_i][prev_j] * 0.125
            dp = dpTemp
    
        res = 0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        return res





















