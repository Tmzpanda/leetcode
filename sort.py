"""
# partition
# sort by parity - partition O(n)
# sort colors
# quick select

# merge
# kClosest O(logn + k)
# intersection - O(m + n)
               - O(m*logn)


# absSort

"""

#********************************* partition **********************************************
# sort by parity
def sortArrayByParity(self, nums):
    l, r = 0, len(nums) - 1

    while l < r:
        while l < r and nums[l] % 2 == 0:
            l += 1
        while l < r and nums[r] % 2 == 1:
            r -= 1
        if l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
    return nums
    

# sort color





#********************************* selection sort **********************************************





    
