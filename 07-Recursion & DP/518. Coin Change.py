
# 518. Coin Change - number of solutions - dp O(n*S)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = dp[i][s - coins[i -1]] + dp[i - 1][s]    # repeated use
#                   dp[i][s] = dp[i - 1][s - coins[i -1]] + dp[i - 1][s]    # used once
                else:
                    dp[i][s] = dp[i - 1][s] 
                    
        return dp[-1][-1]


# 518. Coin Change - number of solutions - dp O(n*S)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = dp[i][s - coins[i -1]] + dp[i - 1][s]    # repeated use
#                     dp[i][s] = dp[i - 1][s - coins[i -1]] + dp[i - 1][s]    # used once
                else:
                    dp[i][s] = dp[i - 1][s] 
                    
        return dp[-1][-1]
