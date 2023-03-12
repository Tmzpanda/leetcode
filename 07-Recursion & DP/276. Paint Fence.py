# 276. Paint Fence - number of solutions - dp O(n)
def numWays(n, k):
    dp = [0] * n
    dp[0], dp[1] = k, k*k

    for i in range(2, n):
        dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])

    return dp[n - 1]