"""
# 139. Word Break 
# 132. Palindrome Partitioning - minimum cut  
# 583. Delete Distance 

# 410. Split Array Largest Sum

"""


# 139. Word Break 
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
      
      
# 132. Palindrome Partitioning - minimum cut   
class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            
            if isPalindrome(s):
                return 0
            
            res = len(s) - 1
            for i in range(len(s)):
                if isPalindrome(s[: i + 1]):
                    res = min(res, 1 + dfs(s[i + 1:], memo))
                    
            memo[s] = res
            return res
        
        return dfs(s, {})
            


# 583. Delete Distance 
def minDistance(word1: str, word2: str) -> int:

    def dfs(word1, word2, memo):
        if (word1, word2) in memo:
            return memo[(word1, word2)]

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)


        if word1[0] == word2[0]:
            res = dfs(word1[1:], word2[1:], memo)

        else:
            res = min(dfs(word1, word2[1:], memo) + 1,
                      dfs(word1[1:], word2, memo) + 1
                     )

        memo[(word1, word2)] = res
        return res

    return dfs(word1, word2, {})


