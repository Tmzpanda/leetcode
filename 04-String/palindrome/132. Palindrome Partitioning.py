# 132. Palindrome Partitioning - minimum cut - dp O(n^2)
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



# 132. Palindrome Partitioning - minimum cut - dp O(n^2)
import sys
class Solution:
    def minCut(self, s):
        return self.dfs(s, {})
        
    def dfs(self, s, memo):
        n = len(s) 
        dp = [sys.maxsize] * n
        
        for i in range(n):
            if self.isPalindrome(s[:i + 1]):
                dp[i] = 0
            else:
                for j in range(i):
                    if self.isPalindrome(s[j + 1: i + 1]):   # s[j + 1 to i]
                        dp[i] = min(dp[i], dp[j] + 1)
                    
        return dp[n - 1]
    
    def isPalindrome(self, s):
        return s == s[::-1]