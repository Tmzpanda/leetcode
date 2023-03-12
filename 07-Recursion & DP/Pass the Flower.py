# Pass the Flower - number of paths - dp O(k*n) 
def find_paths(n, k): 
    dp = [[0] * n for i in range(k + 1)] 
    dp[0][0] = 1 

    for i in range(1,k + 1):
        for j in range(n):
            dp[i][j] = dp[i-1][(j-1+n)%n] + dp[i-1][(j+1+n)%n]

    return dp[k][0]
    
           
# all possible paths - backtrack O(2^m)
def find_paths(n, m): 
    def dfs(i, n, m, path, res):
        if m < 0:
            return 
        
        if m == 0 and i == 0:
            res.append('->'.join(list(path)))
            return 
        
        for j in ((i-1+n)%n, (i+1+n)%n):
            path.append(str(j))
            dfs(j, n, m - 1, path, res)
            path.pop()
            
    res = []
    dfs(0, n, m, [], res)
    return res