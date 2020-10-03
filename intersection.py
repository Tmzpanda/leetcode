"""
intersection - two pointers O(m + n)    - m ≈ n
             - binary search O(m.logn)  - m ≫ n

intersection of two BST

"""
#********************************* intersection of two sorted array **********************************************
# two pointers O(m + n) 
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []

    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res
    
    
# binary search O(m.logn) 
def intersection(arr1, arr2):
    result = []
    
    for num in arr1:
        if binarySearchFound(arr2, num):
            result.append(num)
    return result

def binarySearchFound(nums, target):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            r = mid
        else:
            l = mid

    if nums[l] == target:
        return True
    if nums[r] == target:
        return True
    return False

    
#********************************* intersection of two BST **********************************************







