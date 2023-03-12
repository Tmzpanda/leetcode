# 131. Palindrome Partitioning - all solutions - backtrack
#                                              - memoization
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, substrings, res):
        if not s:
            res.append(substrings[:])
            return 
        
        for i in range(len(s)):
            prefix = s[: i + 1]
            if self.isPalindrome(prefix):
                substrings.append(prefix)
                self.dfs(s[i + 1:], substrings, res)
                substrings.pop()
            
    def isPalindrome(self, s):
        return s == s[::-1]