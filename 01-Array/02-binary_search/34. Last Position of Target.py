# 34. Last Position of Target
def lastPosition(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] <= target:
            l = mid
        else:
            r = mid

    if nums[r] == target:           # specail case: [1, 2, 3, 3]
        return r
    elif nums[l] == target:
        return l
    else:
        return -1