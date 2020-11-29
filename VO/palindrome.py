"""
Longest Common Substring
Longest Common Subsequence


Longest Panlindrome Substring - two pointers
                              - dp
Longest Palindrome Subsequence


K-Palindrome Substring  - dfs
                        - edit distance???
Longest K-Palindrome Substring
    
    
Palindrome Partioning - all possible solutions
                      - minimum cuts
                        
Word Break
Subset
Permutation

"""

#*********************************************************** Palindrome ************************************************************************
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
  
    def longestPalindrome(self, s):
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
def longestPalindrome(s):
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
  
  
  
#*********************************************************** K-Palindrome ************************************************************************
# K-Palindrome Substring
# memoizaiton???
def isKPalindrome(s, k):
    if len(s) == 1:
        return True
    
    while s[0] == s[-1]:
        s = s[1: -1]
        if len(s) <= 1:
            return True
          
    if k == 0:
        return False
    
    return isKPalindrome(s[1:], k - 1) or isKPalindrome(s[:-1], k - 1)

  

# Longest K-Palindrome Substring
def longestKPalindrome(s, k):

    if isKPalindrome(s, k):
        return len(s)
    else:
        return max(longestKPalindrome(s[1:], k), longestKPalindrome(s[:-1], k))
