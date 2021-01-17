"""
# sorted 
# 704. Target
# 34. Last Position of Target
# 702. Search in a Big Sorted Array - first position
# 278. First Bad Version - criteria
# 35. Search Insert Position
# 354. Russian Doll Envelopes - dp O(n^2)
                              - binary search O(nlogn)



# unsorted 
# 153. Find Minimum in Rotated Sorted Array
# 33. Search in Rotated Sorted Array
# 852. Peak Index in a Mountain Array



"""
# ********************************************* sorted array ****************************************************
# Target
def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:     # based on nums[mid]?target
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


# 702. Search in a Big Sorted Array - First Position of Target
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
            
    if reader.get(l) == target:     # special case: [1, 1, 2, 3]
        return l
    elif reader.get(r) == target:
        return r
    else:
         return -1
 
      
# 278. First Bad Version
def findFirstBadVersion(n):
    l, r = 1, n
    while l + 1 < r:
        mid = (l + r) // 2
        if SVNRepo.isBadVersion(mid):     # based on bad_version_or_not
            r = mid
        else:
            l = mid
    
    if SVNRepo.isBadVersion(l): 
        return l
    return r
      
      
# 35. Search Insert Position - K Closest
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


# 354. Russian Doll Envelopes - binary search O(nlogn)
"""
(2, 3), (5, 3), (6, 7), (6, 4)

3, 3, 7, 4

"""
class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
      
        temp = [sys.maxsize] * (len(envelopes) + 1)
        temp[0] = -sys.maxsize
        
        # LIS - binary search O(nlogn)
        longest = 0
        for _, height in envelopes:
            index = self.searchInsert(temp, height)
            temp[index] = height
            longest = max(longest, index)
        
        return longest
    
    def searchInsert(self, nums, target):      
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid
        return r


# 354. Russian Doll Envelopes - dp O(n^2)
class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
            
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [x[1] for x in envelopes]
        
        return self.LIS(heights)
        
    # LIS - dp O(n^2)
    def LIS(self, nums):
        if not nums:
            return 0
        
        n = len(nums)        
        dp = [1] * len(nums)
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)



# ******************************************* unsorted array **********************************************************
# 153. Find Minimum in Rotated Sorted Array
"""
                   o 6
                 o 5
               o 4
             ---------------           
                          o 3
                        o 2  
                      o 1

nums[mid] ? nums[-1]

"""
def findMin(nums):
    
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] <= nums[-1]:    
            r = mid 
        else:     
            l = mid

    if nums[l] < nums[r]:   # special case [1, 2, 3]
        return nums[l]
        
    return nums[r]


# 33. Search in Rotated Sorted Array
def search(nums, target):
    if not A:
        return -1

    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        
        if A[mid] >= A[l]:
            if A[l] <= target <= A[mid]:
                r = mid
            else:
                l = mid       
        else:
            if A[mid] <= target <= A[r]:
                l = mid
            else:
                r = mid

    if A[l] == target:
        return l
    if A[r] == target:
        return r
    
    return -1



# 852. Peak Index in a Mountain Array
"""
                o
              o   o
        o   o
      o   o

nums[mid] ? nums[mid+1]

"""
def findPeak(self, nums):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] < nums[mid + 1]:  
            l = mid
        else:
            r = mid
            
    if nums[l] > nums[r]:     # special case [10, 9, 8, 7]
        return nums[l]
        
    return nums[r]



