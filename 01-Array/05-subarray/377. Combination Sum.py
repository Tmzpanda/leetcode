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


