"""
Longest Common Substring
Longest Common Subsequence


Longest Panlindrome Substring - two pointers
                              - dp
Longest Palindrome Subsequence


K-Palindrome Substring  - dfs
                        - LPS
Longest K-Palindrome Substring
    
    
Palindrome Partioning - all solutions - backtrack
                      - minimum cuts - memoizaiton
                        
Word Break - number of solutions - memoization
           - all solutions - memoization 
Subset
Permutation

"""

#********************************************** Palindrome ************************************************************
# Longest Common Substring O(n^2)
def longestCommonSubstring(A, B):
        
    longest = 0
    for i in range(len(A)):
        for j in range(len(B)):

            l = 0
            while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
                longest = max(longest, l + 1)
                l += 1

    return longest


# Longest Common Subsequence O(n^2)
"""
  "" A G G T A B
"" 0 0 0 0 0 0 0 
G  0 
X  0
T  0
X  0
A  0
Y  0         x = max(dp[i - 1][j], dp[i][j - 1]), when A[i - 1] != B[j - 1]
B  0           x = dp[i - 1][j - 1] + 1, when A[i - 1] == B[j - 1]
"""
def LCS(A, B):
    if not A or not B:
        return 0
        
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n +  1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Longest Panlindrome Substring
# two pointers
class Solution:
  
    def longestPalindromeSubstring(self, s):
        if not s:
            return ""

        longest = ""
        for i in range(len(s)):
            sub1 = self.findPalindrome(s, i, i)
            sub2 = self.findPalindrome(s, i, i + 1)
            sub = max(sub1, sub2, key=lambda x: len(x))
            if len(sub) > len(longest):
                longest = sub

        return longest
    
    def findPalindrome(self, string, l, r):
        while l >= 0 and r < len(string) and string[l] == string[r]:
            l -= 1
            r += 1
        
        l, r = l + 1, r - 1
        return string[l:r + 1]
        
# dp
def longestPalindromeSubstring(s):
    if not s:
        return 0

    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = True
    for i in range(1, n):
        dp[i][i - 1] = True
       
    longest = 0
    start, end = 0, 0
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
            
            if dp[i][j]:
                longest = length
                start, end = i, j
                
    return s[start: end + 1]


# Longest Panlindrome Subsequence
def longestPalindromeSubseq(s):
    if not s:
        return 0

    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
         
    return dp[0][n - 1]
  
  
  
#********************************************* K-Palindrome *************************************************************
# K-Palindrome Substring
# dfs
def isKPalindrome(s, k):
    if len(s) == 1:
        return True
    
    while s[0] == s[-1]:
        s = s[1: -1]
        if len(s) <= 1:
            return True
          
    if k == 0:
        return False
    
    return isKPalindrome(s[1:], k - 1) or isKPalindrome(s[:-1], k - 1)    # memoization

  
# Longest K-Palindrome Substring
def longestKPalindrome(s, k):
    longest = len(LPS(s))
    
    if len(s) - longest <= k
        return longest
    else:
        return max(longestKPalindrome(s[1:], k), longestKPalindrome(s[:-1], k))   # memoization

      
      
#********************************************** Partition *************************************************************
# All Partition Solutions
# backtrack
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
            prefix = s[:i + 1]
            if self.isPalindrome(prefix):
                substrings.append(prefix)
                self.dfs(s[i + 1:], substrings, res)
                substrings.pop()
            
    def isPalindrome(self, s):
        return s == s[::-1]
    

# Minimum Cut
# dfs memoization 
import sys
class Solution:
    def minCut(self, s):
        return self.dfs(s, {})
        
    def dfs(self, s, memo):
        if s in memo:
            return memo[s]
        
        if len(s) <= 1 or self.isPalindrome(s):
            return 0
        
        res = sys.maxsize
        for i in range(len(s)):
            if self.isPalindrome(s[: i + 1]):
                res = min(res, 1 + self.dfs(s[i + 1:], memo))
            
        memo[s] = res
        return res
    
    def isPalindrome(self, s):
        return s == s[::-1]
      
# dp
import sys
class Solution:
    def minCut(self, s):
        n = len(s) 
        palindrome = self.palindrome(s)
        cuts = [sys.maxsize] * n
        
        
        for i in range(n):
            if palindrome[0][i]:
                cuts[i] = 0
            else:
                for j in range(0, i):
                    if palindrome[j + 1][i]:
                        cuts[i] = min(cuts[i], cuts[j] + 1)
                    
        return cuts[n - 1]
                    
    
    def palindrome(self, s):
        if not s:
            return 0
  
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        for i in range(1, n):
            dp[i][i - 1] = True
           
        longest = 0
        start, end = 0, 0
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                
        return dp







