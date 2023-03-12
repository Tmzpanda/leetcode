# 322. Coin Change - fewest coins - dp O(S)
def coinChange(coins, amount):
    
    dp = [sys.maxsize for i in range(amount + 1)]
    dp[0] = 0
    
    for s in range(1, amount + 1):
        for coin in coins:
            if coin <= s:
                dp[s] = min(dp[s], dp[s - coin] + 1)       
    
    return dp[amount] if dp[amount] != sys.maxsize else -1


