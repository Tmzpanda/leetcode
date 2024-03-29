# 494. Assign symbols to Target Sum - number of solutions - dp O(n*S)

def findTargetSumWays(nums, target):
    n = len(nums)
    total_sum = sum(nums)
    if total_sum < target or (total_sum + target) % 2 != 0:
        return 0
    S = (total_sum + target) // 2
    dp = [0] * (S+1)
    dp[0] = 1
    for num in nums:
        for s in range(S, num-1, -1):
            dp[s] += dp[s-num]
    return dp[S]




def findTargetSumWays(nums, target):
    n = len(nums)
    total_sum = sum(nums)
    if total_sum < target or (total_sum + target) % 2 != 0:
        return 0
    S = (total_sum + target) // 2
    dp = [[0] * (S+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(S+1):
            if nums[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    return dp[n][S]
  
  
  
  
  
  
  
  
  
  
"""
nums = [1, 2, 1] -> s = 4
S = 0

                    s
        -4 -3 -2 -1 0 1 2 3 4 
 nums 0  0  0  0  0 0 0 0 0 0
      1
      2           x   x
      1             x = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
                    

"""
def findTargetSumWays(nums, S):
    if sum(nums) < S:
        return 0
    
    n = len(nums)
    s = sum(nums)
    dp = [[0] * (2*s + 1) for _ in range(n + 1)]
    dp[0][s] = 1

    for i in range(1, n + 1):
        for j in range(2*s + 1):
            if j - nums[i - 1] >= 0:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]
            if j + nums[i - 1] <= 2*s:
                dp[i][j] += dp[i - 1][j + nums[i - 1]]
    
    return dp[-1][s + S]
 
