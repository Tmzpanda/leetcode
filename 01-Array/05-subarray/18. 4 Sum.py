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
       
    for i in range(len(nums) - k + 1):  
        if target < nums[i] * k or target > nums[-1] * k:      # trim 
            break

        if i > 0 and nums[i-1] == nums[i]:                     # deduplicate
            continue
         
        subset.append(nums[i])
        dfs(nums[i + 1:], target - nums[i], k - 1, subset, results)
        subset.pop()
        
        
