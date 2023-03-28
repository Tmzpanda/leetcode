# 912. Sort an Array (Merge Sort)
"""
            [1, 2, 3, 4]
           /       ^    \ mid = 2
       [1, 2]          [3, 4]  
       /   ^ \ mid = 1
     [1]     [2] 


            
            [1, 2, 3]
           /    ^    \ mid = 1
        [1]         [2, 3]   
           
"""
# O(nlogn)
def mergeSort(nums: List[int]) -> List[int]:
    # base
    if len(nums) == 1:
        return nums
    
    # divide and conquer
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    # merge
    merged = [0] * len(nums)     
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged       
