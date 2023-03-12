# 35. Search Insert Position
def searchInsert(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid
        else:
            r = mid

    if nums[l] >= target:     # special case
        return l
    if nums[r] >= target:
        return r
    return len(nums)

# K closest  
def findUpperClosest(self, A, target):
    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if target == A[mid]:
            return mid
        elif A[mid] < target:
            l = mid
        else:
            r = mid
                 
    return r