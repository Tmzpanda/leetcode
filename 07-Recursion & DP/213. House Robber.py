# 213. House Robber - cycle
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])    
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     

        for i in range(3, n):
            dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[n - 1], dp2[n - 1])