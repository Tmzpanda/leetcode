

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
        
        
