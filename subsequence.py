"""
# subsequence
# sell stock - greedy O(n)
# LIS  - length - dp O(n^2)
                - binary search O(nlogn)
       - path - dp O(n^2)
# LPS O(n^2)
# LCS - dp O(n^2)


# subset
# Largest Divisible Subset - dp O(n^2)
# Russian Dolls Envelopes - dp(nlogn)

# kSum O(n^(k-1))
# combinationSum - all possible solutions - backtrack O(2^n)
                 - if possible solution exists - dp O(n*S)
                 - number of possible solutions - dp O(n*S)


121. Sell Stock - Subsequence Maximum Diff - one transaction - greedy O(n)
122.                                       - ∞ transactions - greedy O(n) 
188.                                       - at most K transactions - dp 
309.                                       - ∞ transactions with cooldown - 
714.                                       - ∞ transactions with transaction fee -


                             
"""

# sell stock - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit


# sell stock - at most K transactions - O(n^2 * k)
"""
prices = [3,2,6,5,0,3] k = 2

  0 1 2
0 0 0 0
3 0 0 0
2 0 x = max(dp[i - 1][j],
6 0         max(prices[i] - prices[x] + dp[x - 1][j - 1]), where 0 <= x < i
5 0         )
0 0
3 0  

"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for j in range(1, k + 1):
        profit = -sys.maxsize
        
        for i in range(1, n):
            profit = max(profit, -prices[i - 1] + dp[i - 1][j - 1])
            dp[i][j] = max(dp[i - 1][j], prices[i] + profit)

    return dp[-1][-1]
  
  
  
# sell stock - cool down
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
  

# sell stock - transaction fee
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

    print(dp)
    return dp[-1]




