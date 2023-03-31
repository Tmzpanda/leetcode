# 216. Combination Sum III 
# backtrack
def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []
    def dfs(index, k, target, path):
        if k == 0 and target == 0:
            res.append(list(path))
            return
        if target < 0 or k < 0:
            return 

        for i in range(index, 10):
            path.append(i)
            dfs(i+1, k-1, target-i, path)
            path.pop()

    dfs(1, k, n, [])
    return res
