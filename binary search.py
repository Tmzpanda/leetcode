"""
# sorted 
# Target
# Intersection 
# Last Position
# Big Sorted Array
# First Bad Version

# Insert/Upper
# K Closest
# Russian Doll Envelopes




# unsorted 
# Rotated
# Mountain 







"""
#********************************************* sorted array **********************************************************
"""
x x x x x x o
      -
      l     r
        _
        l   r
          -
          l r

nums[mid] ? target

"""

# target
def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid
        else:
            r = mid

    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1


# last position of target
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


# big sorted array - first occurrence of target
def searchBigSortedArray(reader, target):
    index = 0
    while reader.get(index) < target:
        index = index * 2 + 1
        
    l, r  = 0, index
    while l + 1 < r: 
        mid = (l + r) // 2
        
        if target <= reader.get(mid):
            r = mid
        else:
            l = mid
            
    if reader.get(l) == target: # special case [1, 1, 2, 3]
        return l
    elif reader.get(r) == target:
        return r
    else:
         return -1

      
# first bad version
def findFirstBadVersion(n):
    l, r = 1, n
    while l + 1 < r:
        mid = (l + r) // 2
        if SVNRepo.isBadVersion(mid):
            r = mid
        else:
            l = mid
    
    if SVNRepo.isBadVersion(l): # first occurrence special case
        return l
    return r
      
      
# insert place
def findUpperClosest(self, A, target):
    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if target == A[mid]:
            return mid
        elif target < A[mid]:
            r = mid
        else:
            l = mid
    return r



#********************************************* unsorted array **********************************************************
# rotated sorted array 
"""
                   o 6
                 o 5
               o 4
             ---------------           
                          o 3
                        o 2  
                      o 1

nums[mid] ? target=nums[-1]
"""
# find min
def findMin(nums):
    
    l, r = 0, len(nums) - 1
    target = nums[-1]
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] <= target:    
            r = mid 
        else:     
            l = mid

    if nums[l] < nums[r]:   # special case [1, 2, 3]
        return nums[l]
        
    return nums[r]


# mountain sequence
"""
                o
              o   o
        o   o
      o   o

nums[mid] ? nums[mid+1]

"""
# find peak
def findPeak(self, nums):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] < nums[mid + 1]:  
            l = mid
        else:
            r = mid
            
    if nums[l] > nums[r]: # special case [10, 9, 8, 7]
        return nums[l]
        
    return nums[r]



