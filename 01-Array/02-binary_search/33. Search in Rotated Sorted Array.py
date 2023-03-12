
# 33. Search in Rotated Sorted Array
def search(nums, target):
    if not nums:
        return -1

    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        
        if nums[mid] >= nums[l]:
            if nums[l] <= target <= nums[mid]:
                r = mid
            else:
                l = mid       
        else:
            if nums[mid] <= target <= nums[r]:
                l = mid
            else:
                r = mid

    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    
    return -1
