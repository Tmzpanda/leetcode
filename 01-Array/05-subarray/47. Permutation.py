# 47. Permutation
def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)

    def dfs(index):
        if index == n:
            res.append(list(nums))
            return 
        for i in range(index, n):
            nums[index], nums[i] = nums[i], nums[index]
            dfs(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    res = []
    dfs(0)

    return res
