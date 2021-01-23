









# ************************************************* Stock ***********************************************************
# 121. Sell Stock - Subsequence Maximum Diffs - one transaction - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit
  
  
# 122. Sell Stock - Subsequence Maximum Diffs - ∞ transactions - greedy O(n) 
# 188.                                        - at most K transactions - dp O(n*k)
# 309.                                        - ∞ transactions with cooldown - dp O(n)
# 714.                                        - ∞ transactions with transaction fee - dp O(n)








          
        





            










           
            
        

  



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
      






