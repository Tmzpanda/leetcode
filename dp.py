"""
M1 - time complexity
O(n)
# 198. House Robber - dp O(n)
# 91. Decode Ways - dp O(n)

O(n^2) 
# 139. Word Break - if possible - dp O(n^2)
                  - number of solutions - dp O(n^2)
# 300. Longest Increasing Subsequence - O(n^2)
# 354. Russian Doll Envelopes - dp O(n^2)
                              - binary search O(nlogn)
# 368. Largest Divisible Subset - path - dp O(n^2)
# 132. Palindrome Partitioning - minimum cut - dp O(n^2)

O(n*S)
# knapsack
# 416. Partition Equal Subset Sum - if possible - dp O(n*S)
# 518. Coin Change - number of solutions - dp O(n*S)
# 494. Assign symbols to Target Sum - dp O(n*S)

O(k*n) 
# 188. Sell Stock - at most K transactions - dp O(k*n)                         

O(S*n) 
# 377. Combination Sum - different sequences are counted as different combinations - number of solutions - dp O(S*n)
# 322. Coin Change - fewest coins - dp O(S*n)

O(m*n)
# 688. Knight Probability in Chessboard - dp O(K*n^2)
# 221. Maximal Square - dp O(n^2) 
# 62. Unique Paths - dp O(m*n)
# 1143. Longest Common Subsequence - dp O(n^2)                         
# 516. Longest Palindromic Subsequence - dp O(n^2)
# 44. Wildcard Matching - dp O(m*n)

 

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
# 188. Sell Stock - at most K transactions - dp O(k*n)

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
# 198. House Robber - dp O(n)
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1 or len(nums) == 2:
        return max(nums)

    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = nums[0], max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
#         dp[i % 3] = max(nums[i] + dp[(i - 2) % 3], dp[(i - 1) % 3])     # space optimization
        
    return dp[n - 1]
  
  
# 91. Decode Ways - number of solutions - dp O(n)
class Solution:
    def numDecodings(self, s):
        if s.startswith('0'):
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * self.isValid(s[i - 1]) + dp[i - 2] * self.isValid(s[i - 2: i])
            
        return dp[n]
    
    def isValid(self, string):
        n = len(string)
        num = int(string)
        if n == 1 and 1<= num <= 9:
            return 1
        if n == 2 and 10 <= num <= 26:
            return 1
        return 0   
    
    
# ****************************************** O(n^2) **********************************************     
# 139. Word Break - if possible - dp O(n^2)
#                 - number of solutions - dp O(n^2)
def wordBreak(s, wordSet):
       
    n = len(s)
    dp = [False for _ in range(n + 1)] 
    dp[0] = True
   
    for i in range(n + 1):
       for j in range(i + 1, n + 1):
           if dp[i] and s[i: j] in wordDict:
               dp[j] = True
                
#            if s[i: j] in wordSet:         # number of solutions
#                 dp[j] += dp[i] 
                    
    return dp[n]
    
    
# 300. Longest Increasing Subsequence - O(n^2)
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
  
  
# 368. Largest Divisible Subset - path - dp O(n^2)
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
# ****************************************** O(n*S) **********************************************  
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

# 416. Partition Equal Subset Sum - if possible - dp O(n*S)
def canPartition(nums):
    if not nums:
        return False
    
    if sum(nums) % 2 != 0:
        return False

    n = len(nums)
    S = sum(nums) // 2
    
    dp = [[False for _ in range(S + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(1, n + 1):
        for s in range(S + 1):
            if s == 0:
                dp[i][s] = True
            if nums[i - 1] <= s:
                dp[i][s] = dp[i - 1][s - nums[i -1]] or dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]

    return dp[n][S]


# 518. Coin Change - number of solutions - dp O(n*S)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = dp[i][s - coins[i -1]] + dp[i - 1][s]    # repeated use
#                     dp[i][s] = dp[i - 1][s - coins[i -1]] + dp[i - 1][s]    # used once
                else:
                    dp[i][s] = dp[i - 1][s] 
                    
        return dp[-1][-1]


# ************************************** O(S*n) ***************************************************
# 377. Combination Sum - number of solutions - dp O(S*n)
def combinationSum(self, nums, target):
        if not nums:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for s in range(1, target + 1):
            for num in nums:            # different sequences are counted as different combinations       
                if num <= s:
                    dp[s] += dp[s - num]
        
        return dp[target]
      
      
# 322. Coin Change - fewest coins - dp O(S)
def coinChange(coins, amount):
    
    dp = [sys.maxsize for i in range(amount + 1)]
    dp[0] = 0
    
    for s in range(1, amount + 1):
        for coin in coins:
            if coin <= s:
                dp[s] = min(dp[s], dp[s - coin] + 1)        # dp[i][s] = min(dp[i][s - coins[i -1]] + 1, dp[i - 1][s])
    
    return dp[amount] if dp[amount] != sys.maxsize else -1




# ************************************** O(m*n) ***************************************************

# 688. Knight Probability in Chessboard - O(K*n^2)
DIRECTIONS = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), 
               (1, -2), (2, -1), (2, 1), (1, 2)]

class Solution:
    def knightProbability(self, N, K, r, c):
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
    
        for step in range(K):
            dpTemp = [[0 for i in range(N)] for j in range(N)]    
            for i in range(N):
                for j in range(N):
                    for delta_i, delta_j in DIRECTIONS:
                        next_i = i + delta_i
                        next_j = j + delta_j
                        if 0 <= next_i < N and 0 <= next_j < N:
                            dpTemp[next_i][next_j] += dp[i][j] * 0.125
            dp = dpTemp
    
        res = 0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        return res

      
# 221. Maximal Square - dp O(n^2) 
def maximalSquare(matrix):
    if not matrix: 
        return 0
    
    m , n = len(matrix), len(matrix[0])
    dp = [[ 0 if matrix[i][j] == '0' else 1 for j in range(0, n)] for i in range(0, m)]
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                
    res = max(max(row) for row in dp)
#     res = max(map(lambda x: max(x), a))
    return res ** 2 
  
  
# 62. Unique Paths - dp O(m*n)
def uniquePaths(m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][1] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
    return dp[m][n]
 

# 1143. Longest Common Subsequence - dp O(m*n)   
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

