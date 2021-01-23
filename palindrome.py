"""
718. Longest Common Substring - dp O(m*n)
                              - two pointers O(m * n * min(m,n)) TLE
1143. Longest Common Subsequence - dp O(m*n)
5. Longest Panlindrome Substring - two pointers O(n^2)
                                 - dp O(n^2)
516. Longest Palindromic Subsequence - dp O(n^2)

1216. K-Palindrome Substring - LPS
                             - dfs memoization - dp
                             
131. Palindrome Partioning - all solutions - backtrack
132.                       - minimum cuts - memoizaiton - dp

"""


# 718. Longest Common Substring - dp O(m*n)
#                               - two pointers O(m * n * min(m,n)) TLE
# 1143. Longest Common Subsequence - dp O(m*n)

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

      
      




