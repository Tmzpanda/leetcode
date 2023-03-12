# 287. Find the Duplicate Number

# O(1) extra space
def findDuplicates(nums):
    res = []
    
    for num in nums:
        i = abs(num) - 1
        if nums[i] < 0:
            res.append(abs(num))
        nums[i] = - nums[i]   # mark the corresponding entries as negative
        
    return res


# 287. Duplicate Number in an Array 
# sort 
def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            return nums[i]

# value-index mapping
"""
1 ≤ a[i] ≤ n 
0 ≤ index ≤ n - 1
<value, index> exclusive mapping makes O(n) O(1) achievable

"""
def findDuplicates(nums):
    res = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            res.append(abs(nums[i]))
        nums[index] = - nums[index]
        
    return res
