# 516. Longest Palindromic Subsequence - dp O(n^2)
"""
  a d b b c a
a 1         x = dp[i + 1][j - 1] + 2, when s[i] == s[j] 
d   1     x = max(dp[i + 1][j], dp[i][j - 1]), when s[i]! = s[j]
b     1
b       1
c         1
a           1

"""
def LPS(s):
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


