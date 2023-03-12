


# merge sort
def sort(nums):

    def mergeSort(nums, l, r):
        if l >= r:
            return

        mid = (l + r) // 2
        mergeSort(nums, l, mid - 1)
        mergeSort(nums, mid + 1, r)
        merge(nums, l, r)


    def merge(nums, l, r):
        middle = (start + end) // 2
        mergeSort(nums, start, middle)
        mergeSort(nums, middle + 1, end)
        merge(nums, start, end)



# 912. Merge Sort O(nlogn)
def mergeSort(nums):
    if len(nums) == 1:
        return 

    mid = (len(nums) - 1) // 2
    left = nums[:mid + 1]
    right = nums[mid + 1:]
    
    mergeSort(left)
    mergeSort(right)

    # merge
    l, r = 0, 0
    index = 0   
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            nums[index] = left[l]
            l += 1
        else:
            nums[index] = right[r]
            r += 1
        index += 1

    while l < len(left):
        nums[index] = left[l]
        l += 1
        index += 1

    while r < len(right):
        nums[index] = right[r]
        r += 1
        index += 1



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