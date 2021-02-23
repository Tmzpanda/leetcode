"""

# 40. Combination Sum - all solutions - backtrack O(2^n)
# 377. Combination Sum - different sequences are counted as different combinations - number of solutions - dp O(S*n)
# 518. Coin Change - number of solutions - dp O(n*S)
# 416. Partiton Equal Subset Sum - if possible - dp O(n*S)
# 322. Coin Change - fewest coins - dp O(S*n)
# 47. Permutation - O(n!)

# 216. K Sum - all positive - all solutions - backtrack O(2^n)
# 18. K Sum - negative exists - all solutions - two pointers O(n^(k-1))


# 112. Binary Tree Path Sum - if exists - dfs top-down
# 113. Binary Tree Path Sum - all solutions - dfs backtrack
# 437.          Subpath Sum - number of solutions - psum


"""

# ****************************************** Combination Sum **********************************************
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


# 377. Combination Sum - number of solutions - dp O(S*n)
def combinationSum(self, nums, target):
        if not nums:
            return 0
        
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for s in range(1, target + 1):
            for num in nums:            # different sequences are counted as different combinations       
                if num <= s:
                    dp[s] += dp[s - num]
        
        return dp[target]


# 518. Coin Change - number of solutions - dp O(n*S)
# 416. Partiton Equal Subset Sum - if possible - dp O(n*S)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for s in range(1, amount + 1):
                if coins[i - 1] <= s:
                    dp[i][s] = dp[i][s - coins[i -1]] + dp[i - 1][s]    # repeated use
#                     dp[i][s] = dp[i - 1][s - coins[i -1]] + dp[i - 1][s]    # used once
                else:
                    dp[i][s] = dp[i - 1][s] 
                    
        return dp[-1][-1]


# 322. Coin Change - fewest coins - dp O(S)
def coinChange(coins, amount):
    
    dp = [sys.maxsize for i in range(amount + 1)]
    dp[0] = 0
    
    for s in range(1, amount + 1):
        for coin in coins:
            if coin <= s:
                dp[s] = min(dp[s], dp[s - coin] + 1)        
    
    return dp[amount] if dp[amount] != sys.maxsize else -1


              
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
        
        

# ****************************************** K Sum **********************************************
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
        
        
# 18. K Sum - negative exists - all solutions - two pointers O(n^(k-1))
# four sum O(n^3)
def fourSum(nums, target):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(0, n - 3):
        if i > 0 and nums[i] == nums[i - 1]:       # deduplicate
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
                
            s = target - nums[i] - nums[j]
            l, r = j + 1, n - 1
            while l < r:
                if nums[l] + nums[r] == s:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    r -= 1
                    l += 1
                
                    while l < r and nums[l] == nums[l - 1]:         # deduplicate
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > s:
                    r -= 1
                else:
                    l += 1
                
    return res

# K Sum O(n^(k-1))
def kSum(nums, target, k):
    nums.sort()
    
    results = []
    dfs(nums, target, k, [], results)
    return results

def dfs(nums, target, k, subset, results):

    if k == 2:
        l, r = 0, len(nums) - 1 
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(subset + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:        # deduplicate
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return
       
    for i in range(0, len(nums) - k + 1):  
        if target < nums[i] * k or target > nums[-1] * k:      # trim 
            break

        if i > 0 and nums[i-1] == nums[i]:                     # deduplicate
            continue
         
        subset.append(nums[i])
        dfs(nums[i + 1:], target - nums[i], k - 1, subset, results)
        subset.pop()
        
        



