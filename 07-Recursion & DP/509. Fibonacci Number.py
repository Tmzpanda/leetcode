# 509. Fibonacci Number
# memoization
def fib(n: int) -> int:
    memo = {}
    def dfs(n):
        # memo
        if n in memo:
            return memo[n]
        # base
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # transition
        memo[n] = dfs(n - 1) + dfs(n - 2)
        return memo[n]
    
    return dfs(n - 1) + dfs(n - 2)
  
    
# another way
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n-1) + fib(n-2)
 
  
# dp
def fib(n: int) -> int:
    # edge
    if n == 0:
        return 0
    if n == 1:
        return 1

    # base
    dp = [0] * (n + 1)
    dp[1] = 1
    # transition
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
