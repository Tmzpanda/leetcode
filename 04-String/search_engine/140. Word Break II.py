# 140. Word Break - all possible sentences
# memoization
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    memo = {}
    def dfs(s):
        # memo
        if s in memo:
            return memo[s]
        # base
        if not s:
            return []

        res = []
        for i in range(len(s)): 
            if s[:i+1] in wordDict:
                word_breaks = dfs(s[i+1:])
                for word in word_breaks:
                    res.append(s[:i+1] + " " + word)
                if i+1 == len(s):
                    res.append(s[:i+1])

        memo[s] = res
        return memo[s]

    return dfs(s)
 
    
# dp 
def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    word_set = set(wordDict)
    n = len(s)
    # base
    dp = [[] for _ in range(n+1)]
    dp[0] = ['']

    for i in range(1, n+1):
        for j in range(i):
            if s[j:i] in word_set:
                for word in dp[j]:
                    dp[i].append(word + ' ' + s[j:i] if word else s[j:i])

    return dp[-1]
