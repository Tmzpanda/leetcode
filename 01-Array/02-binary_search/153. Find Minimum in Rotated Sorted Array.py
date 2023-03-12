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
