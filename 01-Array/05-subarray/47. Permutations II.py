# 47. Permutations II - duplicate exists

def permute(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    def dfs(index):
        if index == n:
            res.append(list(nums))

        used = set()
        for i in range(index, n):
            if nums[i] in used:
                continue

            used.add(nums[i])       # deduplicate
            nums[index], nums[i] = nums[i], nums[index]
            dfs(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    
    res = []
    dfs(0)
    return res
