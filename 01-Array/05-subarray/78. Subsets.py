# 78. Subsets

def subsets(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)

    def dfs(index, subset):
        res.append(list(subset))
        for i in range(index, n):
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

    res = []
    dfs(0, [])

    return res

