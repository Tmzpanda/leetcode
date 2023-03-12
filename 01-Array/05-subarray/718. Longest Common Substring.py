
# 718. Longest Common - Substring - O(m * n * min(m,n)) TLE
def longestCommonSubstring(A, B):
        
    longest = 0
    for i in range(len(A)):
        for j in range(len(B)):
            
            l = 0
            while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
                longest = max(longest, l + 1)
                l += 1
            
    return longest



# dp O(n^2)
def longestCommonSubstring(A, B):
        
        if not A or not B:
            return 0
        
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n +  1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
        return max(map(max, dp))
