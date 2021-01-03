"""
# 139. Word Break - if possible
#                 - number of solutions
# 91. Decode Ways
# 70. Climbing Stairs

# 198. House Robber
# 322. Coin Change

# Longest Increasing Subsequence
# Sell Stock
# 30天


# dp升维
# 滚动降为
# 成立/几种/最x的一种/具体方案


# tree path sum
# subset combination sum

# bfs 图 
course schedule
number of islands

# ood


"""

#**************************************************  ***************************************************
# 139. Word Break - if possible
#                 - number of solutions
# dfs memoization
class Solution:

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return True
        
        res = False
        for i in range(0, len(s)):
            if s[:i + 1] in wordDict and self.dfs(s[i + 1:], wordDict, memo) == True:
                res = True
#                 res += self.dfs(s[i + 1:], wordDict, memo)    # number of solutions
                
        memo[s] = res      
        return res

      
# dp
class Solution:
    def wordBreak(self, s, wordDict):
       
        n = len(s)
        dp = [False for _ in range(n + 1)] 
        dp[0] = True

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i: j] in wordDict:
                    dp[j] = True  
#                     dp[j] += dp[i]    # number of solutions
                    
        return dp[n]
  

#**************************************************  ***************************************************
# 198. House Robber - max amount
# dfs memoization
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        
        return self.dfs(nums, len(nums) - 1, {})
        
    
    def dfs(self, nums, i, memo):
        if i in memo:
            return memo[i]
        
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        
        res = max(self.dfs(nums, i - 2, memo) + nums[i], 
                  self.dfs(nums, i - 1, memo))
            
        memo[i] = res
        return res
       
        
# dp       
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]













    

