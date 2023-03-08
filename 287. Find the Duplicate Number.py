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
