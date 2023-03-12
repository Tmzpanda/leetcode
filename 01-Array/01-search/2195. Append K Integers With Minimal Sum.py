# 2195. Append K Integers With Minimal Sum

# O(n) TLE
def minimalKSum(nums: List[int], k: int) -> int:
    nums.sort() 
    
    i, target = 0, 1
    res = 0
    
    while i < len(nums):
        if nums[i] == target:
            i += 1
            target += 1
        elif nums[i] > target:
            res += target
            k -= 1
            if k == 0:
                return res
            target += 1
        else:
            i += 1  # deduplicate

    while k > 0:
        res += target
        target += 1
        k -= 1

    return res
  


