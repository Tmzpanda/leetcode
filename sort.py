"""
# partition
# 905. Sort Array By Parity - partition O(n)
# 75. Sort Colors - partition O(n)
# 215. Kth Largest Element in an Array - quick select O(n)    
# 347. Top K Frequent Elements - sort O(nlogn)
#                              - heap O(nlogk)
# 973. K Closest Points to Origin - heap O(nlogk)      
# 912. Quick Sort O(nlogn)



# merge
# 658. K Closest Elements in a Sorted Array - binary search merge O(logn + k) 
# 272. K Closest BST Values - recursion O(n)
                            - binary search + iterator O(logn + k)
# 349. Intersection of Two Arrays - two pointers O(m + n)
                                  - binary search O(m * logn)
# 4. Median (Kth) of Two Sorted Arrays - merge O(m + n)
                                       - binary search O(m + n)         X
# 912. Merge Sort O(nlogn)
# 23. Merge k Sorted Lists - O(Nlogn), where n is # of LinkedLists, N is # of nodes



# Duplicate
# 287. Duplicate Number in an Array - sort O(nlogn) O(1)
                                    - set  O(n) O(n)
                                    - value-index mapping O(n) O(1)
# 448. Find Disappeared Numbers in an Array - value-index mapping O(n) O(1)

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
# quick select O(n)
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int):      # k -> n-k+1 -> n-k
        n = len(nums)
        return self.quickSelect(nums, 0, n - 1, n - k)
        
    
    def quickSelect(self, nums, start, end, k):
        if start == end:            
            return nums[k]
        
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

        if k <= r:
            return self.quickSelect(nums, start, r, k)
        if k >= l:
            return self.quickSelect(nums, l, end, k)

        return nums[k]



# 347. Top K Frequent Elements   
# sort O(nlogn)
def topKFrequent(nums, k):
  
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    freq_dict_sorted = sorted(freq_dict.items(), key=lambda x: -x[1])
    
    res = []
    for i in range(k):
        res.append(freq_dict_sorted[i][0])
        
    return res
  
  
# heap O(nlogn)
from heapq import heappush, heappop
def topKFrequent(nums, k):
        
    freq_dict = {}
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    heap = []
    for item in freq_dict.items():
        heappush(heap, (item[1], item[0]))
        if len(heap) > k:
            heappop(heap)
            
    res = []
    while len(heap) > 0:
        freq, num = heappop(heap)
        res.append(num)
        
    res.reverse()
    return res



  
  
# 973. K Closest Points to Origin - heap O(nlogk) 
 class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        origin = [0, 0]
        
        heap = []
        for point in points:
            distance = self.getDistance(point, origin)
            heapq.heappush(heap, (-distance, point[0], point[1]))   # function as max heap 

            if len(heap) > K:
                heapq.heappop(heap)

        output = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            output.append([x, y])

        output.reverse()
        return output
    
    
    def getDistance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 
      
      
# 912. Quick Sort O(nlogn)
def quickSort(nums, start, end):
    
    if start >= end:      # break condition 
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
# 658. K Closest Elements in a Sorted Array - binary search merge O(logn + k)    
class Solution:
    def kClosestNumbers(self, A, target, k):
        r = self.findUpperClosest(A, target)
        l = r - 1
    
        res = []
        for _ in range(k):
            if self.isLeftCloser(A, target, l, r):
                res.append(A[l])
                l -= 1
            else:
                res.append(A[r])
                r += 1
                
        return res
    
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
        
    def isLeftCloser(self, A, target, l, r):
        if l < 0:
            return False
        if r >= len(A):
            return True
          
        return target - A[l] <= A[r] - target




# 349. Intersection of Two Arrays - two pointers O(m + n)
#                                 - binary search O(m * logn)
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
    
    
# binary search O(n.logm)  
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




#******************************************** Duplicate *********************************************************
# 287. Duplicate Number in an Array 
# sort 
def findDuplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            return nums[i]

# set 
def deduplicate(nums):
    index = 1
    traversed = set()
    for i in range(len(nums)):
        if i > 0 and nums[i] not in traversed:
            nums[index] = nums[i]
            index += 1
        traversed.add(nums[i])

    return nums[:index]

# value-index mapping
"""
1 ≤ a[i] ≤ n 
0 ≤ index ≤ n - 1
<value, index> exclusive mapping makes O(n) O(1) achievable

"""
def findDuplicates(nums):
    res = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            res.append(abs(nums[i]))
        nums[index] = - nums[index]
        
    return res


# 448. Find Disappeared Numbers in an Array - O(n) O(1)
def findDisappearedNumbers(nums):
    res = []
    
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = - nums[index]

    return [index + 1 for index in range(len(nums)) if nums[index] > 0]

    
