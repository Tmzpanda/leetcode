# 216. K Sum - all positive - all solutions - backtrack O(2^n)
class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
       
        res = []
        self.dfs(1, target, [], k, res)
        return res

    def dfs(self, index, target, subset, k, res):
        if target < 0 or k < 0:
            return 
        
        if k == 0 and target == 0:
            res.append(list(subset))
            return
        
        for i in range(index, 10):
            subset.append(i)
            self.dfs(i + 1, target - i, subset, k - 1, res)
            subset.pop()
