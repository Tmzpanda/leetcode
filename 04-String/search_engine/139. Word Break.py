# 139. Word Break
# memoization
def wordBreak(s: str, wordDict: List[str]) -> bool:
    memo = {}
    def dfs(s):
        # memo
        if s in memo:
            return memo[s]
        # base
        if not s:
            return True

        for i in range(len(s)):
            word = s[:i+1]
            if word in wordDict and dfs(s[i+1:]) == True:
                memo[s] = True
                return memo[s]
                
        memo[s] = False
        return memo[s]

    return dfs(s)



# 139. Word Break 
# dp 
def wordBreak(s: str, wordDict: List[str]) -> bool:
    # base
    n = len(s)
    dp = [False] * (n+1)
    dp[0] = True
    
    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True

    return dp[n]
