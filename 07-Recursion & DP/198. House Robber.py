# 198. House Robber - array        
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
#           dp[i % 3] = max(nums[i] + dp[(i - 2) % 3], dp[(i - 1) % 3])     # space optimization

        return dp[n - 1]



# 198. Rob House - dp O(n)
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