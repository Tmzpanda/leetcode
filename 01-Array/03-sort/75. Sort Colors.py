# 75. Sort Colors - partition O(n)
"""
2 0 2 0 1 0   
l         r
^

0 0 2 0 1 2    
l       r
^

0 0 2 0 1 2
    l   r
    ^  
    
0 0 1 0 2 2    
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
    i = 0

    while i <= r:
        if nums[i] == 0:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1