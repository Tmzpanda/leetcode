# 256. Paint House - minimum cost - dp O(n*k)
def minCost(costs):
        
    n, k = len(costs), len(costs[0])
    dp = [[0] * k for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(k):
            dp[i][j] = costs[i - 1][j] + min(dp[i-1][(j-1 + 3)%3], dp[i-1][(j+1 + 3)%3])

    return min(dp[-1])