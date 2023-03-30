# 40. Combination Sum - all solutions - backtrack O(2^n)
class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []
        self.dfs(nums, 0, target, [], result)
        return result
        
    def dfs(self, nums, index, target, subset, result):
        if target < 0:
            return 
        
        if target == 0:
            result.append(list(subset)) 
            return
        
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, target - nums[i], subset, result)   # used once
#             self.dfs(nums, i, target - nums[i], subset, result)     # repeated use
#             self.dfs(nums, target - nums[i], subset, result)        # different sequences are counted as different combinations
            subset.pop()
