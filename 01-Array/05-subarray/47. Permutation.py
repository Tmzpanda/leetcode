# 47. Permutation - O(n!)
class Solution:
    def permutation(self, nums):
        nums.sort()
        used = [False] * len(nums)
        result = []
        self.dfs(nums, used, [], result)
        return result
        
    def dfs(self, nums, used, path, result):
        if len(path) == len(nums):
            result.append(list(path)) 
            return 
        
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):       # deduplicate
                continue
                
            used[i] = True
            self.dfs(nums, used, path + [nums[i]], result)   
            used[i] = False