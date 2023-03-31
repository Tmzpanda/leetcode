# 40. Combination Sum II
def combinationSum2(nums: List[int], target: int) -> List[List[int]]:
    nums = sorted(nums)
    res = []

    def dfs(target, index, combination):
        if target == 0:
            res.append(list(combination)) 
            return
        if target < 0:
            return 

        for i in range(index, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue
            combination.append(nums[i])
            dfs(target - nums[i], i + 1, combination)   # used once
#             dfs(target - nums[i], i, combination)       # repeated use
#             dfs(target - nums[i], combination)          # combinations in different orders are considered different
            combination.pop()

    dfs(target, 0, [])

    return res
