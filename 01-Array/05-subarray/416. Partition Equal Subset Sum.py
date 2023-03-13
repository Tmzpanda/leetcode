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