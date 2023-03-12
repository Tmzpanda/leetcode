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
