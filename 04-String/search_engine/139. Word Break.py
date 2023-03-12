# 139. Word Break - dp O(n^2)
def wordBreak(s, wordDict):
    
    def dfs(s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return 1
    
        res = 0
        for i in range(len(s)):
            if s[: i + 1] in wordDict:
                res += dfs(s[i + 1:], wordDict, memo)
                
        memo[s] = res
        return res
    
    return dfs(s, wordDict, {})



# 139. Word Break - if possible - dp O(n^2)
#                 - number of solutions - dp O(n^2)
def wordBreak(s, wordSet):
       
    n = len(s)
    dp = [False for _ in range(n + 1)] 
    dp[0] = True
   
    for i in range(n + 1):
       for j in range(i + 1, n + 1):
           if dp[i] and s[i: j] in wordDict:
               dp[j] = True
                
#            if s[i: j] in wordSet:         # number of solutions
#                 dp[j] += dp[i] 
                    
    return dp[n]


# 139. Word Break - if possible - dp O(n^2)
#                 - number of solutions - dp O(n^2)
def wordBreak(s, wordSet):
       
    n = len(s)
    dp = [False for _ in range(n + 1)] 
    dp[0] = True
   
    for i in range(n + 1):
       for j in range(i + 1, n + 1):
           if dp[i] and s[i: j] in wordDict:
               dp[j] = True
                
#          if s[i: j] in wordSet:         # number of solutions
#              dp[j] += dp[i] 
                    
    return dp[n]