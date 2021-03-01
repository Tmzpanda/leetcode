
"""
iterator
# 230. Kth Smallest Element in a BST - iterator O(k)
# 999. Intersection of two BST - m ≈ n - recursion merge O(m + n)   
                                       - iteration merge O(m + n)    
                               - m ≫ n - binary search O(n.logm)
                          
# 270. Closest BST Value - binary search O(logn)
# 272. K Closest BST Values - recursion O(n)
                            - binary search + iterator O(logn + k)
                            

operation
# 450. Delete Node in a BST

"""
# ******************************************* SMALLEST ********************************************************* 
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

  
# Intersection of two BST 
# recursion O(m + n)  
class Solution:
    def intersection(self, root1, root2):
        arr1, arr2 = [], []
        self.traverse(root1, arr1)
        self.traverse(root2, arr2)
        
        # merge
        i, j = 0, 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
                
        return result
    
    def traverse(self, root, arr):
        if not root:
            return
        self.traverse(root.left, arr)
        arr.append(root.val)
        self.traverse(root.right, arr)

        
# iteration O(m + n)  
class Solution:
    def intersection(self, root1, root2):
        stack1, stack2 = [], []
        self.getSuccessor(stack1, root1)
        self.getSuccessor(stack2, root2)
        
        res = []
        while stack1 and stack2:
            if stack1[-1].val < stack2[-1].val:
                node = stack1.pop()
                self.getSuccessor(stack1, node.right)
            elif stack1[-1].val > stack2[-1].val:
                node = stack2.pop()
                self.getSuccessor(stack2, node.right)
            else:
                node = stack1.pop()
                self.getSuccessor(stack1, node.right)
                res.append(node.val)
                      
        return res

    def getSuccessor(self, stack, root):
        while root:
            stack.append(root)
            root = root.left
            
            
# ******************************************* CLOSEST *********************************************************            
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
        
        

# ******************************************* Operation *********************************************************      
# 450. Delete Node in a BST
def delete_node(root, val):
    if not root:
        return

    if root.val > val:
        root.left = delete_node(root.left, val)
    elif root.val < val:
        root.right = delete_node(root.right, val)

    else:
        #  No Child or One Child
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # Two children -> Find min node in right-subtree, copy the value, delete min node from right-subtree
        else:
            temp = find_smallest(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)
            
    return root

  
def find_smallest(root):
    while root.left:
        root = root.left
        
    return root
