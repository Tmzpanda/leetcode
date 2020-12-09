"""

# 2 sum - closest
        - data structure
        
        
        
# One Possible Solution
# 2Sum - hashmap
       - 2 pointers (if sorted)
# 3Sum
# 4Sum
# kSum
  
  
# All Possible Solutions - deduplicate
# 4Sum 
# kSum 
# combinationSum 

39. Combination Sum - all solutions - repeated use - backtrack O(2^n)
40.                                 - deduplicate num exists - backtrack O(2^n)
377.                - number of solutions - different sequences are different combinations - dp O(n*S)
416. Partiton Equal Subset Sum - if possible - dp O(n*S)

216. K Sum - positive - all solutions - backtrack O(2^n)
                      - number of solutions - dp O(n*S*K)
18.        - negative exists - all solutions - two pointers O(n^(k-1))


"""


# 39 Combination Sum
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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
            subset.append(nums[i])
            self.dfs(nums, i, target - nums[i], subset, result) # unique combinations, repeated use
            subset.pop()

# 40. Combination Sum
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
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
            if i != 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, target - nums[i], subset, result)   # used once
            subset.pop()


# 377. Combination Sum
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        result = []
        self.dfs(nums, target, [], result)
        return len(result)
        
        
    def dfs(self, nums, target, subset, result):
        if target < 0:
            return 
        
        if target == 0:
            result.append(list(subset)) 
            return
        
        for i in range(len(nums)):
            subset.append(nums[i])
            self.dfs(nums, target - nums[i], subset, result) # different sequence are counted as different combinations
            subset.pop()


# 216. K Sum
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
        
        
# 90. Subset 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.dfs(nums, 0, [], result)
        return result
        
        
    def dfs(self, nums, index, subset, result):
 
        result.append(list(subset)) 
        
        for i in range(index, len(nums)):
            if i != 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, result)   # used once
            subset.pop()
        
              
# 47. Permutation
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            self.dfs(nums, used, path + [nums[i]], result)   # used once
            used[i] = False
       
       
 # 60. Kth Permutation Sequence



# *********************************** One Possible Solution ***************************************
# two sum
# hashmap O(n) O(n) 
def twoSum(nums, target):
    num_to_index = {}
    for index, num in enumerate(nums):
        if target - num in num_to_index:
            return [num_to_index[target - num], index]
        num_to_index[num] = index
   
   
# two pointers - if sorted O(n) O(1)
def twoSum(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l, r]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return -1


""""
sort array
arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
       i           i
          j           j                  (arr[i], arr[j], where i < j)
            [4, 0, 9, 5, 1, 3], s = 11   (complementing pair in the subarray - twoSum)
            
""""
# four sum O(n^3)
def fourSum(arr, s):
    arr.sort()
    n = len(arr)
    
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            target = s - (arr[i] + arr[j])
            
            # two sum
            l, r = j + 1, n - 1
            while l < r:
                if arr[l] + arr[r] == target:
                    return [arr[i], arr[j], arr[l], arr[r]]
                elif arr[l] + arr[r] > target:
                    r -= 1
                else:
                    l += 1       
    return []


# k sum O(n^(k-1))
def kSum(nums, target, k):
    nums.sort()
    
    results = []
    dfs(nums, target, k, [], results)
    return results[0]

def dfs(nums, target, k, subset, results):
    
    if len(results) == 1:         # break
        return

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
        
        
arr = [2, 7, 4, 0, 9, 5, 1, 3, 3]
s = 20
k = 4
kSum(arr, s, k)


# *********************************** All Possible Solutions ****************************************
# four sum 
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


# k sum
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
        
        
arr = [2, 7, 4, 0, 9, 5, 1, 3, 3]
s = 20
k = 4
kSum(arr, s, k)


# Combination Sum - O(2^n)
class Solution:

    def combinationSum(self, nums, target):
        nums.sort()
        
        results = []
        self.dfs(nums, 0, target, [], results)
        return results

    def dfs(self, nums, index, target, subset, results):
        if target == 0:
            results.append(list(subset))                # deep copy
            return

        if target < 0:
            return
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:    # deduplicate
                continue
            
            subset.append(nums[i])
            self.dfs(nums, i + 1, target - nums[i], subset, results)
            subset.pop()





  
