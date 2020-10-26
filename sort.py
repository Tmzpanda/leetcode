"""
# partition
# sort by parity - partition O(n)
# sort colors - partition O(n)
# kth smallest/largest - quick select - partition O(n)
# quick sort - O(nlogn)




# merge
# kClosest O(logn + k)
# intersection - O(m + n)
               - O(m*logn)
# merge sort - O(nlogn)
# merge range - O(Nlogn), where n is # of linked lists, N is # of nodes



"""

#******************************************** partition *********************************************************
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
"""
          1 3 2 5 7  pivot = 5, k = 2
                lr
                
          1 3 2      pivot = 2
            l r 
          1 2 3  
            r l
            
              3      pivot = 3
             r l     return 

"""
def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        return partition(nums, start, r, k)
    if k >= l:
        return partition(nums, l, end, k)
        
    return nums[k]


# quick sort O(nlogn)
"""
1 4 3     >3                  1 4 3     >=3    
  l r                         r l

1 3 4
  r l
  
  
  
3 4 3     >3
l   r

3 4 3
r l
  
  4 3 
  l r
  
  3 4
  r l
  
"""
def quickSort(nums, start, end):
    
    if start >= end:
        return

    l, r = start, end
    pivot = nums[random.randint(l, r)]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    quickSort(nums, start, r)
    quickSort(nums, l, end)
    
#******************************************** merge *********************************************************
# merge sort
"""
            [1, 4, 3, 5, 7]
    [1, 4, 3]             [5, 7]
 [1, 4]    [3]           [5]  [7]
[1]  [4]     


"""
 def mergeSort(nums):
    if len(nums) == 1:
        return 

    mid = (len(nums) - 1) // 2
    left = nums[:mid + 1]
    right = nums[mid + 1:]
    mergeSort(left)
    mergeSort(right)

    l, r = 0, 0
    index = 0   
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            nums[index] = left[l]
            l += 1
        else:
            nums[index] = right[r]
            r += 1
        index += 1

    while l < len(left):
        nums[index] = left[l]
        l += 1
        index += 1

    while r < len(right):
        nums[index] = right[r]
        r += 1
        index += 1


# merge range - O(Nlogn), where n is # of linked lists, N is # of nodes
"""
   o -> o -> ... -> o      vs     1
   o -> o -> ... -> o             4
   .                              3
   .                              5
   o -> o -> ... -> o             7

no extra space                   extra space
return                           no return

"""

def mergeNLists(lists):
    return mergeRange(lists, 0, len(lists) - 1)

def mergeRange(lists, start, end):
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = mergeRange(lists, start, mid)
    right = mergeRange(lists, mid + 1, end)
    return merge(left, right)
  
def merge(l1, l2): 
    temp = dummy = ListNode(0)
    p1, p2 = l1, l2
    while p1 or p2:
        if isFirstPointerSmaller(p1, p2):
            temp.next = p1
            p1 = p1.next
        else:
            temp.next = p2
            p2 = p2.next
        temp = temp.next

    return dummy.next

def isFirstSmaller(p1, p2):
    if p1 is None:
        return False
    if p2 is None:
        return True
    return p1.val <= p2.val







    
