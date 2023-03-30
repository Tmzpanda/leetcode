# 518. Coin Change II - number of solutions
# dp O(n*S)
def coinChange(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in coins:          # order differences are considered the same solution
        for s in range(coin, amount + 1):
            dp[s] += dp[s - coin]

    return dp[amount]

