"""
# subsequence
# sell stock - greedy O(n)
# LIS  O(n^2) - length
              - path
# LPS O(n^2)
# LCS - 1d array - dp O(n^2)
      - 2d matrix 
# Largest Divisible Subset - dp O(n^2)



# subset
# kSum O(n^(k-1))
# combinationSum - all possible solutions - backtrack O(2^n)
                 - if possible solution exists - dp O(n*S)
                 - number of possible solutions - dp O(n*S)



# Minimum Window Subsequence - dp O(ST)
                             - two pointers O(ST) = O((# of pattern found)*S*T)
                             
"""

# sell stock - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit




  
  
  
  
# Minimum Window Subsequence 
# dp - O(S*T)
"""
        "" X Y
      "" 0 ∞ ∞ 
      G  0 
      X  0 
      T  0 
      X  0 
      A  0 
      Y  0   x = dp[i - 1][j - 1] + 1, when S[i - 1] == T[j - 1]
      B  0   x = dp[i - 1][j] + 1,     when S[i - 1] != T[j - 1]

dp[i][j] represents window length of S which contains T[0 to j - 1]
"""
def minWindow(S, T):
        
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range (m + 1)]
    for j in range(1, n + 1):
        dp[0][j] = sys.maxsize 

    for i in range(1, m + 1):
        for j in range(1, n +  1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = dp[i - 1][j] + 1

    minLen = sys.maxsize
    for i in range(1, m + 1):
        if dp[i][n] < minLen:
            minLen = dp[i][n]
            end = i - 1

    if minLen == sys.maxsize:
        return ""

    return S[end - minLen + 1: end + 1]


# two pointers - O((# of pattern found)*S*T) = O(ST)
def minWindow(S, T):
        
    minLen = len(S) + 1
    window = ""

    i, j = 0, 0
    while i < len(S):
        if S[i] == T[j]:
            j += 1
        if j == len(T):
            end = i 
            j -= 1
            while j >= 0:
                if S[i] == T[j]:
                    j -= 1
                i -= 1
            i += 1
            j += 1
            if end - i + 1< minLen:
                minLen = end - i + 1
                window = S[i:end + 1]
        i += 1
    return window
  










