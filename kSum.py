"""
# 2Sum - hashmap
       - 2 pointers (if sorted)
  3Sum
  4Sum
  kSum
  
# kSum (all possible solutions - deduplicate)
# combinationSum 

"""

# ************************ One Possible Solution ***************************************
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


# ************************ All Possible Solutions ****************************************
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


# ************************ Combination Sum - All Possible Solutions ****************************************
# O(2^n)
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





  
