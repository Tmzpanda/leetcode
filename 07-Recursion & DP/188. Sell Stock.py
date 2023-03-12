# 188. Sell Stock - at most K transactions - dp O(k*n)
  
"""
prices = [3,2,6,5,0,3] k = 2

  3 2 6 5 0 3
0 0 0 0 0 0 0 
1 0 x = max(dp[i][j - 1],
2 0         max(prices[j] - prices[x] + dp[i - 1][x - 1]), where 0 <= x < j


"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        profit = -sys.maxsize
        
        for j in range(1, n):
            profit = max(profit, -prices[j - 1] + dp[i - 1][j - 1]) # greedy
            dp[i][j] = max(dp[i][j - 1], prices[j] + profit)

    return dp[-1][-1]



# 188. Sell Stock - at most K transactions - dp O(k*n)
  
"""
prices = [3,2,6,5,0,3] k = 2
  3 2 6 5 0 3
0 0 0 0 0 0 0 
1 0 x = max(dp[i][j - 1],
2 0         max(prices[j] - prices[x] + dp[i - 1][x - 1]), where 0 <= x < j
"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        profit = -sys.maxsize
        
        for j in range(1, n):
            profit = max(profit, -prices[j - 1] + dp[i - 1][j - 1]) # greedy
            dp[i][j] = max(dp[i][j - 1], prices[j] + profit)

    return dp[-1][-1]