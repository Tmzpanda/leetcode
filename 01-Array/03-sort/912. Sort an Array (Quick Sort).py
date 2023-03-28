

# 912. Quick Sort O(nlogn)
def quickSort(nums, start, end):
    
    if start >= end:      # break condition 
        return

    l, r = start, end
    pivot = random.randint(l, r)

    # partition
    while l <= r:
        while l <= r and nums[l] < nums[pivot]:
            l += 1
        while l <= r and nums[r] > nums[pivot]:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    quickSort(nums, start, r)
    quickSort(nums, l, end)
