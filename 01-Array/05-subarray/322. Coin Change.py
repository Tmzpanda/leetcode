# 322. Coin Change - fewest coins
# dp O(n*S), O(S)
def coinChange(coins, amount):
    dp = [sys.maxsize for _ in range(amount + 1)]
    dp[0] = 0
    
    for coin in coins:
        for s in range(coin, amount + 1):
            dp[s] = min(dp[s], dp[s - coin] + 1)  
    
    return dp[amount] if dp[amount] != sys.maxsize else -1
