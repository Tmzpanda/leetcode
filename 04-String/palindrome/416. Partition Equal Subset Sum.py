# 416. Partition Equal Subset Sum - dp O(n*S)
def canPartition(nums):
    
    if sum(nums) % 2 != 0 or max(nums) > sum(nums)//2:
            return False

    n = len(nums)
    S = sum(nums) // 2

    def dfs(nums, target, memo):
        if target in memo: 
            return memo[target]

        if target < 0: 
            return False
        if target == 0: 
            return True

        res = False
        for i in range(len(nums)):
            if dfs(nums[i+1:], target-nums[i], memo): 
                res = True

        memo[target] = res
        return res

    return dfs(nums, S, {})
