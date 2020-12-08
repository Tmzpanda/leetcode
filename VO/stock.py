# sell stock
# coin change
# rob house




# 518. coin change
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

        
