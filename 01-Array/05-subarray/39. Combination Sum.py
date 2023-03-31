# 39. Combination Sum
def combinationSum(nums: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(target, index, combination):
        if target == 0:
            res.append(list(combination)) 
            return
        if target < 0:
            return 

        for i in range(index, len(nums)):
            combination.append(nums[i])
            dfs(target - nums[i], i, combination)   # each can be used infinite times
            combination.pop()

    dfs(target, 0, [])
    return res
