# O(n*W)
# dp  
"""
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7

      w
      0 1 2 3 4 5 6 7
 wt 0 0 0 0 0 0 0 0 0
    1 0
    3 0
    4 0   o         o
    5 0             x = dp[i][w] denotes the maximum value that can be obtained by selecting from the first i items, subject to a weight capacity of w.
"""
def knapSack(wt, val, W): 
    n = len(wt)
    dp = [[0] * (W + 1) for _ in range(n + 1)] 
    
    for i in range(1, n + 1): 
        for w in range(1, W + 1): 
            if wt[i-1] <= w: 
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W] 


# space optimization
def knapSack(wt, val, W):
    n = len(wt)
    dp = [0 for _ in range(W + 1)]
    
    for i in range(1, n + 1):
        for w in range(W, wt[i] - 1, -1):
            if wt[i-1] <= w:
                dp[w] = max(val[i-1] + dp[w-wt[i-1]], dp[w])
    
    return dp[W]
