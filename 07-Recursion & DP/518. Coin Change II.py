# 518. Coin Change II - number of solutions
# dp O(n*S), O(S)
def coinChange(amount: int, coins: List[int]) -> int:
    dp = [0 for _ in range(amount + 1)]
    dp[0] = 1

    for coin in coins:          # combinations in different orders are considered the same
        for s in range(coin, amount + 1):
            dp[s] += dp[s - coin]

    return dp[amount]

