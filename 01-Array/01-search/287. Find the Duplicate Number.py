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


# sort 
def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            return nums[i]

