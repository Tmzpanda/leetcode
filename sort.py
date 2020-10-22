"""
# partition
# sort by parity - partition O(n)
# sort colors
# kth largest
# quick sort



# merge
# kClosest O(logn + k)
# intersection - O(m + n)
               - O(m*logn)
# merge sort
# merge range



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
"""
2 0 2 0 1 0     nums[index] == 2: switch(nums[index], nums[r]), r--
l         r
^

0 0 2 0 1 2     nums[index] == 0: switch(nums[index], nums[l]), l++ index++
l       r
^

0 0 2 0 1 2
    l   r
    ^  
    
0 0 1 0 2 2     nums[index] == 1: index++
    l r
    ^
  
0 0 1 0 2 2    
    l r
      ^
      
0 0 0 1 2 2
      lr
        ^
"""
def sortColors(nums):
        
    l, r = 0, len(nums) - 1
    index = 0

    while index <= r:
        if nums[index] == 0:
            nums[index], nums[l] = nums[l], nums[index]
            l += 1
            index += 1
        elif nums[index] == 2:
            nums[index], nums[r] = nums[r], nums[index]
            r -= 1
        else:
            index += 1


# Kth smallest
# sort O(nlong)
# heap O(nlogk)
# quick select - partition O(n)


#********************************* merge **********************************************










#********************************* selection sort **********************************************





    
