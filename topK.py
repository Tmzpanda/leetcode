"""
Array
# 215. Kth Largest Element in an Array - quick select O(n)
# 658. K Closest Elements in a Sorted Array - binary search O(logn + k)

# 347. Top K Frequent Elements - sort O(nlogn)
#                              - heap O(nlogk)
#                              - quick select O(n)
# 973. K Closest Points to Origin - heap O(nlogk)



BST
# 230. Kth Smallest Element in a BST - iterator O(k)
# 270. Closest BST Value - binary search O(logn)
# 272. K Closest BST Values - recursion O(n)
                            - binary search + iterator O(logn + k)

"""

# ************************************************************ Array *********************************************************************
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
  
  
# 973. K Closest Points to Origin
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
  
  
# 658. K Closest Elements in a Sorted Array - binary search O(logn + k)  
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
  
  
  
# ************************************************************ BST *********************************************************************
# 230. Kth Smallest Element in a BST - iterator O(k)
def kthSmallest(root, k):
    stack = []
    node = root
    while node:     
        stack.append(node)
        node = node.left
        
    for i in range(k):
        node = stack.pop()
        res = node.val
        
        node = node.right
        while node:        
            stack.append(node)
            node = node.left
            
    return res

# 270. Closest BST Value - binary search O(logn)
def closestValue(root, target):
    p1, p2 = None, None
  
    node = root
    while node:
        if target > node.val:
            p1 = node
            node = node.right
        elif target < node.val:
            p2 = node
            node = node.left
        else:
            return node.val
 
    return min(p1.val, p2.val, key=lambda x: abs(x - target))



# 272. K Closest BST Values - recursion O(n)
def kClosestValues(root, target, k):
    res = deque()

    def rec(root):        # traverse
        if root is None:
            return
        rec(root.left)
        if len(res) == k:
            if not abs(target - root.val) < abs(target - res[0]):
                return
            res.popleft()
        res.append(root.val)
        rec(root.right)

    rec(root)
    return list(res)
  
 
# binary search + iterator O(logn + k)
"""
                   5 <            BST = [2, 3, 4, 5, 6, 7, 8]
                 /   \            target = 6.1
                3     7 <
               / \   / \
              2   4 6   8
                    ^
          
          
- closest itreator                   
stack = path = [5, 7, 6]
lower               upper                result
[5, 7, 6]           [5, 7]               6
[5]                                      7
                    [5, 7, 8]            5
[5, 3, 4]                                8
                    []                   4 
[5, 3]                                   3
[5, 3, 2]                                2
[]



- smallest iterator
getSuccessor              pop
[5, 3, 2]                 2
                          3
[5, 4]                    4
                          5
[7, 6]                    6
                          7
[8]                       8
[]

"""
class Solution:
    
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
        
        # binary search
        path = self.pathToTarget(root, target) # path = [5, 7, 6] 
        stack = list(path) 
        if stack[-1].val < target:
            self.getSuccessor(stack)           
            upperStack = stack          # upper [5, 7]
            lowerStack = path           # lower [5, 7, 6]
        else:
            self.getPredecessor(stack)
            lowerStack = stack
            upperStack = path
        
        # merge
        result = []
        for i in range(k):
            if self.isPredecessorCloser(lowerStack, upperStack, target):
                result.append(lowerStack[-1].val)
                self.getPredecessor(lowerStack) 
            else:
                result.append(upperStack[-1].val)
                self.getSuccessor(upperStack)
                
        return result
        
    def pathToTarget(self, root, target):   # O(logn)
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
                
        return stack
        
    def getSuccessor(self, stack):     # successor
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
                
    def getPredecessor(self, stack):   # predecessor
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
                
    def isPredecessorCloser(self, lowerStack, upperStack, target):
        if not lowerStack:
            return False
            
        if not upperStack:
            return True
            
        return target - lowerStack[-1].val <= upperStack[-1].val - target



