"""
# d&q
# LCA in BST - iteration O(logn)
# LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
# LCA in Binary Tree - node may not exist - d&q


# traverse recursion
# K Closest Values in a BST - inorder O(n)
# All nodes Distance K in a Binary Tree - preorder O(n)


# BST iterator
# K Smallest Values in a BST - O(k)
# K Closest Values in a BST - O(logn + k)


# serialization & deserialization 

"""


#************************************************** LCA ***************************************************
# LCA in BST
def lowestCommonAncestorInBST(root, p, q):
    node = root
    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < root.val and q.val < root.val:
            node = node.left
        else:
            return node
    
    return None

  
# LCA in Binary Tree
"""""""""
(3,5) -> 4

            4 (4)
           / \
      (3) 3   7 (5)
             / \
        (5) 5   6(None)
        
"""""""""
def lowestCommonAncestor(root, A, B): 

    if root is None:
        return None
        
    if root is A or root is B:                      
        return root
        
    left = self.lowestCommonAncestor(root.left, A, B)   
    right = self.lowestCommonAncestor(root.right, A, B)
    
    if left is not None and right is not None:     
        return root
    if left is not None:                            
        return left
    if right is not None:                        
        return right
    return None  
  
 
# LCA in Binary Tree - node may not exist
"""""""""
(3,9) -> None

                      4 (T, F, 3) -> None
                     / \
          (T, F, 3) 3   7 (F, F, None)
                       / \
         (F, F, None) 5   6(F, F, None)
        
"""""""""
class Solution:

    def lowestCommonAncestor3(self, root, A, B):
        
        a, b, lca = self.helper(root, A, B) 
        if a and b:                                         
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        leftA, leftB, left = self.helper(root.left, A, B)
        rightA, rightB, right = self.helper(root.right, A, B)
        
        a = leftA or rightA or root == A
        b = leftB or rightB or root == B
        
        if root is A or root is B:                           
            return a, b, root
            
        if left and right:
            return a, b, root
        if left:                        
            return a, b, left
        if right:                 
            return a, b, right

        return a, b, None 


# Invert a Binary Tree
def invertTree(root):
    if not root:
        return
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    
    return root

   
#****************************************** closest value in a BST ********************************************** 
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
 
    return min(p1.val, p2.val, key=lambda x: abs(x - target))


#****************************************** k closest values in a BST **********************************************    
# recursion O(n)
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




# iteration two stakcs O(logn + k)
"""
                   5 <            BST = [2,3,4, 5, 6,7,8]
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


#****************************************** k smallest **********************************************
# k smallest elements in a BST 
# iterator
def kthSmallest(root, k):
    stack = []
    node = root
    while node:     # getSuccessor
        stack.append(node)
        node = node.left
        
    for i in range(k):
        node = stack.pop()
        res = node

        node = node.right
        while node:         # getSuccessor
            stack.append(node)
            node = node.left
            
    return res.val





#****************************************** serialization **********************************************
# serialization & deserialization 
# bfs
class Codec:

    @staticmethod
    def serialize(root):
        if root is None:
            return ""

        # use bfs to serialize the tree
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)

        while bfs_order[-1] == '#':
            bfs_order.pop()

        return "[%s]" % ','.join(bfs_order)  # "[8,3,10,1,6,#,14,#,#,4,7,13]"

    @staticmethod
    def deserialize(data):

        if data == "[]":
            return None

        vals = data[1:-1].split(',')  # ['8', '3', '10', '1', '6', '#', '14', '#', '#', '4', '7', '13']
        root = TreeNode(int(vals[0]))
        queue = [root]
        index = 0
        is_left_child = True

        for val in vals[1:]:
            if val is not '#':
                node = TreeNode(int(val))
                if is_left_child:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not is_left_child:
                index += 1

            is_left_child = not is_left_child

        return root
    
   
# dfs
class Codec:

    def serialize(self, root):
        def dfs(root):
            if not root:
                res.append("None,")
                return 
            res.append(str(root.val)+",")
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return "".join(res)

    def deserialize(self, data):
        def helper(q):
            if q[0] == "None":
                q.popleft()
                return
            root = TreeNode(q.popleft())
            l = helper(q)
            r = helper(q)
            root.left = l
            root.right = r
            return root
        
        lst = data.split(",")
        q = collections.deque(lst)
        return helper(q)
