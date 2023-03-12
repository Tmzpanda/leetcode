# 714. Sell Stock - ∞ transactions with transaction fee - dp O(n)
"""
  1, 3, 2, 8, 4, 9
0 0  x = max(dp[i - 1],
             prices[i] - prices[x] - 2 + dp[x - 1], where 0 <= x < i
             )
  
"""
def maxProfit(prices, fee):
        
    n = len(prices)
    dp = [0] * (n + 1)

    profit = -sys.maxsize
    for i in range(2, n + 1):
        profit = max(profit, -prices[i - 1 - 1] - fee + dp[i - 1 - 1])
        dp[i] = max(dp[i - 1], prices[i - 1] + profit)

    return dp[-1]
