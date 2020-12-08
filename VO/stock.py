# sell stock
# coin change
# rob house
"""

322. Coin Change - Combination Sum - number of solutions - dp O(n*S)
518.                               - fewest coins - dp O(S*n)


39. Combination Sum  - number of solutions - different sequences are different combinations - dp O(S*n)
416. Partiton Equal Subset Sum - if possible - dp O(n*S)

216. K Sum - positive - all solutions - backtrack O(2^n)
                      - number of solutions - dp O(n*S*K)
18.        - negative exists - all solutions - two pointers O(n^(k-1))


"""

# 518. coin change - number of solutions
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        n = len(coins)
        dp = [[False for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = dp[i][s - coins[i -1]] + dp[i - 1][s]
                else:
                    dp[i][s] = dp[i - 1][s]
                    
        return dp[-1][-1]
  
# 322. Coin Change - fewest coins

import sys
class Solution:
    def coinChange(self, coins, amount):
    
        dp = [sys.maxsize for i in range(amount + 1)]
        dp[0] = 0
        for s in range(1, amount + 1):
            for coin in coins:
                if coin <= s:
                    dp[s] = min(dp[s], dp[s - coin] + 1)
        
        return dp[amount] if dp[amount] != sys.maxsize else -1
    
    
import sys
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        n = len(coins)
        dp = [[sys.maxsize for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            dp[i][0] = 0
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = min(dp[i][s - coins[i -1]] + 1, dp[i - 1][s])
                else:
                    dp[i][s] = dp[i - 1][s]
                    
        return dp[-1][-1] if dp[-1][-1] != sys.maxsize else -1

        

        
        
        
