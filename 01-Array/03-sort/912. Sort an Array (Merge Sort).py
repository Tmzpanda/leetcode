# 912. Sort an Array (Merge Sort)
# O(nlogn)
def mergeSort(nums: List[int]) -> List[int]:
    # base
    if len(nums) <= 1:
        return nums
    
    # divide and conquer
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    # merge
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums
