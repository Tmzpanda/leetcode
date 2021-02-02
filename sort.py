"""
# partition
# 905. Sort Array By Parity - partition O(n)
# 75. Sort Colors - partition O(n)
# 215. Kth Largest Element in an Array - quick select O(n)
# 347. Top K Frequent Elements - quick select O(n)
# 912. Quick Sort O(nlogn)



# merge
# 658. K Closest Elements in a Sorted Array - binary search merge O(logn + k)    
# 349. Intersection of Two Arrays - two pointers O(m + n)
                                  - binary search O(m * logn)
# 912. Merge Sort O(nlogn)
# 23. Merge k Sorted Lists - O(Nlogn), where n is # of LinkedLists, N is # of nodes



"""

#******************************************** partition *********************************************************
# 905. Sort Array By Parity - partition O(n)
def sortArrayByParity(nums):
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


# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int):      # k -> n-k+1 -> n-k
        n = len(nums)
        return self.quickSelect(nums, 0, n - 1, n - k)
        
    
    def quickSelect(self, nums, start, end, k):     # wrong
        l, r = start, end
        pivot = (l + r) // 2

        # partition
        while l <= r:
            while l <= r and nums[l] < nums[pivot]:
                l += 1
            while l <= r and nums[r] > nums[pivot]:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if k <= r:
            return self.quickSelect(nums, start, r, k)
        if k >= l:
            return self.quickSelect(nums, l, end, k)

        return nums[k]

      
# 912. Quick Sort O(nlogn)
def quickSort(nums, start, end):
    
    if start >= end:
        return

    l, r = start, end
    pivot = random.randint(l, r)

    # partition
    while l <= r:
        while l <= r and nums[l] < nums[pivot]:
            l += 1
        while l <= r and nums[r] > nums[pivot]:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    quickSort(nums, start, r)
    quickSort(nums, l, end)
    
#******************************************** merge *********************************************************
# 912. Merge Sort O(nlogn)
def mergeSort(nums):
    if len(nums) == 1:
        return 

    mid = (len(nums) - 1) // 2
    left = nums[:mid + 1]
    right = nums[mid + 1:]
    
    mergeSort(left)
    mergeSort(right)

    # merge
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


# 23. Merge k Sorted Lists - O(Nlogn), where n is # of LinkedLists, N is # of nodes
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
    while p1 and p2:
        if p1.val <= p2.val:
            temp.next = p1
            p1 = p1.next
        else:
            temp.next = p2
            p2 = p2.next
        temp = temp.next
        
    temp.next = p1 or p2
    
    return dummy.next 







    
