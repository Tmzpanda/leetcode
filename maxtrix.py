"""
# matrix
# Spiral Matrix
# Maximal Sqaure


# chessboard
# Knight



"""



#********************************* Matrix ****************************************
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





#********************************* Chessboard ****************************************
# Unique Paths O(m*n)
def uniquePaths(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
    return dp[m][n]




