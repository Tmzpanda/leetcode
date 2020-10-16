"""
# k closest numbers in a sorted array   - O(logn + k)

# closest value in a BST    - O(logn)
# k closest values in a BST    - recursion O(n)
                               - recursion two stacks O(n)
                               - two stacks iterator  O(logn + k)

# k closest Points - heap
"""

#********************************* k closest numbers in a sorted array **********************************************
# iteration O(logn + k)
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
    
    
#********************************* closest value in a BST ********************************************** 
# iteration O(logn)
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
 
    return min(p1.val, p2.val, key = lambda x: abs(x - target))


#********************************* k closest values in a BST **********************************************    
# recursion O(n)
def kClosestValues(root, target, k):
    res = deque()

    def rec(root):
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


# recursion two stacks O(n)
def closestKValues(root, target, k):
    res = []
    predecessors, successors = [], []
    
    inorderTraverse(root, predecessors, target)
    reverseInorderTraverse(root, successors, target)
    
    for _ in range(k):
        if isPredecessorSmaller(predecessors, successors):
            res.append(predecessors.pop())
        else:
            res.append(successors.pop())
            
    return res


def inorderTraverse(node, predecessors, target):
    if not node:
        return 
    
    inorderTraverse(node.left, predecessors, target)
    if node.val >= target:
        return
    predecessors.append(node.val)
    inorderTraverse(node.right, predecessors, target)
    
    
def reverseInorderTraverse(node, successors, target):
    if not node:
        return 
    
    reverseInorderTraverse(node.right, successors, target)
    if node.val < target:
        return
    successors.append(node.val)
    reverseInorderTraverse(node.left, successors, target)
    
    
def isPredecessorSmaller(predecessors, successors):
    if not predecessors:
        return False
    if not successors:
        return True
    return target - predecessors[-1] <= successors[-1] - target



# iteration two stakcs O(logn + k)
class Solution:
    
    def closestKValues(self, root, target, k): # BST = [2,3,4, 5, 6,7,8]
        if root is None or k == 0:
            return []
        
        path = self.pathToTarget(root, target) # path = [5, 7, 6] target = 6.1
        stack = list(path) 
        if stack[-1].val < target:
            self.getSuccessor(stack)           
            upperStack = stack          # upper [5, 7]
            lowerStack = path           # lower [5, 7, 6]
        else:
            self.getPredecessor(stack)
            lowerStack = stack
            upperStack = path
        
        result = []
        for i in range(k):
            if self.isPredecessorCloser(lowerStack, upperStack, target):
                result.append(lowerStack[-1].val)
                self.getPredecessor(lowerStack) #  lower [5]
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



















