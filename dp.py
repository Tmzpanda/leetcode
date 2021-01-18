"""
M1 - time complexity
O(n)
# 198. House Robber - dp O(n)
# 91. Decode Ways - dp O(n)

O(n^2) 
# 139. Word Break - if possible - dp O(n^2)
# 300. Longest Increasing Subsequence - O(n^2)
# 354. Russian Doll Envelopes - dp O(n^2)
                              - binary search O(nlogn)
# 368. Largest Divisible Subset - path - dp O(n^2)

O(n*S)
# knapsack
# 416. Partiton Equal Subset Sum - if possible - dp O(n*S)
# 518. Coin Change - number of solutions - dp O(n*S)

O(S*n) 
# 377. Combination Sum - different sequences are counted as different combinations - number of solutions - dp O(S*n)
# 322. Coin Change - fewest coins - dp O(S*n)

O(m*n)
# 688. Knight Probability in Chessboard - O(K*n^2)
# 221. Maximal Square - dp O(n^2) 
# 62. Unique Paths - dp O(m*n)
# 1143. Longest Common Subsequence - dp O(n^2)                         
# 516. Longest Palindromic Subsequence - dp O(n^2)

 


M2 - dp
if possible -> "or"
# 416. Partiton Equal Subset Sum - if possible - dp O(n*S)

number of solutions -> "+"
# 518. Coin Change - number of solutions - dp O(n*S)

fewest -> "min()"
# 300. Longest Increasing Subsequence - dp O(n^2)
# 322. Coin Change - fewest coins - dp O(S*n)





M3 - return
dp[n]
# 198. House Robber - dp O(n)
# 322. Coin Change - fewest coins - dp O(S*n)

max(dp)
# 300. Longest Increasing Subsequence - dp O(n^2)
# 221. Maximal Square - dp O(n^2)



                         
space optimization:
dp[i][j] only depends on previous row, so we can optimize the space by using 2 rows instead of the matrix

      w
      0 1 2 3 4 5 6 7
 wt 0 0 0 0 0 0 0 0 0
    1 0
    3 0
    4 0   #         #
    5 0             x =  max(dp[i-1][w-wt[i-1]] + val[i-1], dp[i-1][w]), when wt[i-1] <= w
    
 
"""

# ****************************************** O(n) **********************************************
# Fibonacci
def fib(n):   
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
    

    
# 198. House Robber - dp O(n)
def rob(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    
    n = len(nums)
    dp = [0 for _ in range(n + 1)]
    dp[1], dp[2] = nums[0], max(nums[0], nums[1])
    
    for i in range(3, n + 1):
        dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
    
    return dp[n]
    
    
# 213. House Robber - houses are arranged in a circle - O(n)
def rob2(nums):
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)

    n = len(nums)
    dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
    dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])     # nums[0: n -1]
    dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     # nums[1: n]

    for i in range(3, n):
        dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
        dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

    return max(dp1[n - 1], dp2[n - 1])
    
    
# knapsack  O(n*S)
"""
wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
W = 7

      w
      0 1 2 3 4 5 6 7
 wt 0 0 0 0 0 0 0 0 0
    1 0
    3 0
    4 0     x = dp[i-1][w], when wt[i - 1] > w
    5 0             x =  max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]), when wt[i-1] <= w
    
"""

def knapSack(wt, val, W): 
    n = len(wt)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                dp[i][w] = 0
                
            elif wt[i-1] <= w: 
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], 
                               dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W] 


# combinationSum - if possible solution exists  O(n*S)
def combinationSum(arr, S):
    n = len(arr)
    dp = [[False for _ in range(S + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        for s in range(S + 1):
            if s == 0:
                dp[i][s] = True
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i -1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
   
    return dp[n][S]


# combinationSum - number of possible solutions O(n*S)
def combinationSum(arr, S):
    n = len(arr)
    dp = [[0 for _ in range(S + 1)] for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for s in range(S + 1):
            if s == 0:
                dp[i][s] = 1
            if arr[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - arr[i -1]] + dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]
    
    return dp[n][S]


#****************************************************** Longest Subsequence ***********************************************************
# Longest Increasing Subsequence  O(n^2)
def LIS(nums):
    if not nums:
        return 0
    
    n = len(nums)        
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)
  
  
# path
def LIS(nums):
    if not nums:
        return 0
    
    n = len(nums)        
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    longest, index = 0, -1      
    for i in range(len(nums)):
        if dp[i] > longest:
            longest = dp[i]
            index = i
    
    path = []
    while index != -1:
        path.append(nums[index])
        index = prev[index]
    
    return path[::-1]


# Longest Palindrome Subsequence O(n^2)
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
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                
    return dp[0][n - 1]


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


  
# Largest Divisible Subset - dp O(n^2)
def largestDivisibleSubset(nums):
    if not nums:
        return []
    
    nums.sort()
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] % nums[i] == 0:
                if dp[i] + 1 > dp[j]:
                    dp[j] = dp[i] + 1
                    prev[j] = i
      
    path = []
    longest = max(dp)
    index = dp.index(longest)

    while index != -1:
        path.append(nums[index])
        index = prev[index]
        
    return path[::-1]
    

# Russian Doll Envelopes
# dp O(n^2)
# binary search O(nlogn)
class Solution:
    def maxEnvelopes(self, envelopes):

        if not envelopes:
            return 0
            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        temp = [float('inf')] * (n + 1)
        temp[0] = -float('inf')
        
        longest = 0
        for _, h in envelopes:
            index = self.searchInsert(temp, h)
            temp[index] = h
            longest = max(longest, index)
        
        return longest
    
    
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid
        return r








