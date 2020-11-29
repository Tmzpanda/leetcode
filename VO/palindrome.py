

"""
Longest Common Substring
Longest Common Subsequence





K-Palindrome
Longest Panlindrome Substring - LPS - two pointers
                                    - DP
                                - remove K characters
                                    - dfs
                                    - edit distance???
                                - remove a substring

Longest Palindrome Subsequence

Palindrome Partioning - all possible solutions
                      - minimum cuts
                        
Word Break

Subset
Permutation

"""

#*********************************************************** ************************************************************************
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

