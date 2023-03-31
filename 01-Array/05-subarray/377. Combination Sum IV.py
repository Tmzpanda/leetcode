# 377. Combination Sum IV - number of solutions 
# dp O(S*n), O(S)
def combinationSum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for s in range(1, target + 1):
        for num in nums:            # combinations in different orders are considered different
            if num <= s:
                dp[s] += dp[s - num]
                
    return dp[target]


