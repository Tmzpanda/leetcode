# knapsack  O(n*S)
"""
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7

      w
      0 1 2 3 4 5 6 7
 wt 0 0 0 0 0 0 0 0 0
    1 0
    3 0
    4 0     x = dp[i-1][w], when wt[i - 1] > w
    5 0             x =  max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]), when wt[i-1] <= w
    
"""
def knapSack(wt, val, W): 
    n = len(wt)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                dp[i][w] = 0
                
            elif wt[i-1] <= w: 
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], 
                               dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W] 


def knapsack(W, wt, val):
    # Initialize a table to store the maximum value that can be obtained using the first i items and a knapsack with a maximum capacity of j
    n = len(wt)
    dp = [[0 for j in range(W + 1)] for i in range(n + 1)]
    
    # Iterate over each item and each possible knapsack capacity
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # If the current item cannot be included in the knapsack, skip it
            if wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            # Otherwise, choose the maximum value between including the current item and excluding it
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wt[i - 1]] + val[i - 1])
    
    # Return the maximum value that can be obtained using all the items and a knapsack with a maximum capacity of W
    return dp[n][W]

