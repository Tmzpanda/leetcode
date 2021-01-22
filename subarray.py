"""
329. Longest Increasing Subarray - 2d - dp   ????????

718. Longest Common - Substring - dp O(m*n)
1143.               - Subsequence - dp O(n^2)   
5. Longest Palindromic - Substring - 2pointers O(n^2)                  
516.                   - Subsequence - dp O(n^2)


121. Sell Stock - Subsequence Maximum Diffs - one transaction - greedy O(n)


"""

# Longest Increasing Subarray 2d
# dfs memoization
"""
        0 1 2 3 4..... n
      0     #
      1   # x #
      2     #
      3      
      4
      .
      .
      m

""" 
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = self.dfs(matrix, i, j,  memo)
                
        return max(map(max, dp))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_prev, y_prev = x - delta_x, y - delta_y
            if not self.isValid(matrix, x_prev, y_prev) or matrix[x][y] <= matrix[x_prev][y_prev]:
                continue
            longest = max(longest, self.dfs(matrix, x_prev, y_prev, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
      
      
      

# Longest Palindrome Substring - middle out O(n^2)
class Solution:
    def LPS(self, s):
        if not s:
            return ""
        
        longest = ""
        for middle in range(len(s)):
            sub1 = self.findPalindrome(s, middle, middle)
            sub2 = self.findPalindrome(s, middle, middle + 1)
            sub = max(sub1, sub2, key=lambda x: len(x))
            if len(sub) > len(longest):
                longest = sub
                
        return longest
        
    def findPalindrome(self, string, l, r):
        while l >= 0 and r < len(string):
            if string[l] != string[r]:
                break
            l -= 1
            r += 1
        
        l, r = l + 1, r - 1
        return string[l:r + 1]
          
        
# dp O(n^2)
"""
  a d b b c a
a T         x = s[i] == s[j] && dp[i + 1][j - 1]
d T T     
b   T T
b     T T
c       T T
a         T T
"""
def LPS(s):
      if not s:
          return ""

      n = len(s)
      dp = [[False] * n for _ in range(n)]

      for i in range(n):
          dp[i][i] = True
      for i in range(1, n):
          dp[i][i - 1] = True

      start, end = 0, 0
      longest = 1
      for length in range(1, n):        
          for i in range(n - length):
              j = i + length
              dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
              if dp[i][j]:
                  longest = length + 1
                  start, end = i, j

      return s[start:end + 1]




            




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
  




           
            
        

  
# sell stock - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit


# sell stock - at most K transactions - O(n^2 * k)
"""
prices = [3,2,6,5,0,3] k = 2

  0 1 2
0 0 0 0
3 0 0 0
2 0 x = max(dp[i - 1][j],
6 0         max(prices[i] - prices[x] + dp[x - 1][j - 1]), where 0 <= x < i
5 0         )
0 0
3 0  

"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for j in range(1, k + 1):
        profit = -sys.maxsize
        
        for i in range(1, n):
            profit = max(profit, -prices[i - 1] + dp[i - 1][j - 1])
            dp[i][j] = max(dp[i - 1][j], prices[i] + profit)

    return dp[-1][-1]
  
  
  
# sell stock - cool down
"""
     3 2 6 5 0 3
 0 0 0 x = max(dp[i - 1],
               prices[i] - prices[x] + dp[x - 2], where 0 <= x < i
              )
     
"""
import sys
def maxProfit(prices):
    n = len(prices)
    dp = [0] * (n + 2)

    profit = -sys.maxsize
    for i in range(3, n + 2):
        profit = max(profit, -prices[i - 2 - 1] + dp[i - 1 - 2])
        dp[i] = max(dp[i - 1], prices[i - 2] + profit)

    return dp[-1]
  

# sell stock - transaction fee
"""
  1, 3, 2, 8, 4, 9
0 0  x = max(dp[i - 1],
             prices[i] - prices[x] - 2 + dp[x - 1], where 0 <= x < i
             )
  
"""
def maxProfit(prices, fee):
        
    n = len(prices)
    dp = [0] * (n + 1)

    profit = -sys.maxsize
    for i in range(2, n + 1):
        profit = max(profit, -prices[i - 1 - 1] - fee + dp[i - 1 - 1])
        dp[i] = max(dp[i - 1], prices[i - 1] + profit)

    print(dp)
    return dp[-1]





  # 198. House Robber - array        
class Solution:
    def rob(self, nums):
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

# 213. House Robber - cycle
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])     # nums[0: n -2]
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     # nums[1n -1]

        for i in range(3, n):
            dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[n - 1], dp2[n - 1])

      
# 337. tree
class Solution:
    def rob(self, root):
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)
        
    def visit(self, root):
        if root is None:
            return 0, 0
        
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob
      






