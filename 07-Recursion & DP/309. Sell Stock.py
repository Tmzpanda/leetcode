# 309. Sell Stock - ∞ transactions with cooldown - dp O(n)
"""
     3 2 6 5 0 3
 0 0 0 x = max(dp[i - 1],
               prices[i] - prices[x] + dp[x - 2], where 0 <= x < i
              )
     
"""
import sys
def maxProfit(prices):
    n = len(prices)
    dp = [0] * (n + 2)

    profit = -sys.maxsize
    for i in range(3, n + 2):
        profit = max(profit, -prices[i - 2 - 1] + dp[i - 1 - 2])
        dp[i] = max(dp[i - 1], prices[i - 2] + profit)

    return dp[-1]
