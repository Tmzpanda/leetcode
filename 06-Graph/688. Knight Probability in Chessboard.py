# 688. Knight Probability in Chessboard - O(K*n^2)
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
                    for delta_i, delta_j in DIRECTIONS:
                        next_i = i + delta_i
                        next_j = j + delta_j
                        if 0 <= next_i < N and 0 <= next_j < N:
                            dpTemp[next_i][next_j] += dp[i][j] * 0.125
            dp = dpTemp
    
        res = 0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        return res