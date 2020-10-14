"""
# Spiral Matrix 
# Maximal Sqaure - dp O(m*n)
# Number of Islands - bfs


# Unique Paths - dp O(m*n)
# Knight Probability in Chessboard - O(K*n^2)

"""

#********************************* Matrix ****************************************
# Spiral Matrix
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


# Number of Islands
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


#********************************* Chessboard ****************************************
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

def knightProbability(N, K, r, c):

    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[r][c] = 1

    for step in range(1, K + 1):
        dpTemp = [[0 for i in range(N)] for j in range(N)]    
        for i in range(N):
            for j in range(N):
                if dp[i][j]:    
                    for direction in DIRECTIONS:
                        next_i, next_j = i + direction[0], j + direction[1]
                        if 0 <= next_i < N and 0 <= next_j < N:
                            dpTemp[next_i][next_j] += dp[i][j] * 0.125
        dp = dpTemp

    res = 0
    for i in range(N):
        for j in range(N):
            res += dp[i][j]
    return res






















