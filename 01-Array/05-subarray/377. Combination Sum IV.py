# 377. Combination Sum IV - number of solutions 
# dp O(S*n)
def combinationSum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for s in range(1, target + 1):
        for num in nums:            # order differences are considered different solutions 
            if num <= s:
                dp[s] += dp[s - num]
                
    return dp[target]


