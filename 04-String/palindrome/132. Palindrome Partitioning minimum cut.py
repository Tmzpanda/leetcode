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