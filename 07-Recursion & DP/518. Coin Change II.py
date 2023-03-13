# 518. Coin Change II - number of solutions

# dp O(n*S)
def coinChange(amount: int, coins: List[int]) -> int:
    
    n = len(coins)
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for i in range(n):
        for s in range(coins[i], amount + 1):
            dp[s] += dp[s - coins[i]]

    return dp[amount]

