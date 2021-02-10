"""
# d&q
# 226. Invert Binary Tree - O(n)
# 235. LCA in BST - iteration O(logn)
# 236. LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
# 578. LCA in Binary Tree - may not exist - d&q O(n) O(n)
# 112. Binary Tree Path Sum - if exists
# 437. Binary Tree Subpath Sum - number of solutions - psum
            

# traverse 
# 257. Binary Tree Paths - all solutions  
# 113. Binary Tree Path Sum - all solutions
# 272. K Closest BST Values - inorder traverse O(n)
                            - iterator O(logn + k)
                            
# 102. Binary Tree Level Order Traversal - bfs
# 297. Serialize and Deserialize Binary Tree - dfs
                                             - bfs
                                             

"""


#***************************************** d&q ***************************************************
# 226. Invert Binary Tree
def invertTree(root):
    if not root:
        return
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    
    root.left, root.right = root.right, root.left
    
    return root


# 235. LCA in BST - iteration O(logn)
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

  
# 236. LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
"""
(3,5) -> 4

            4 (4)
           / \
      (3) 3   7 (5)
             / \
        (5) 5   6(None)
        
"""
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
  
 
# 578. LCA in Binary Tree - may not exist - d&q O(n) O(n)
"""
(3,9) -> None

                      4 (T, F, 3) -> None
                     / \
          (T, F, 3) 3   7 (F, F, None)
                       / \
         (F, F, None) 5   6(F, F, None)
        
"""
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


# 112. Binary Tree Path Sum - if exists
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        
        return self.dfs(root, target)
    
    def dfs(self, node, target):
        if not node:
            return target == 0
            
        if target < 0:
            return False
            
        return self.dfs(node.left, target - node.val) or self.dfs(node.right, target - node.val)
      

# 437. Binary Tree Subpath Sum - number of solutions - psum
# bottom-up
class Solution:
    def pathSum(self, root, target):
        self.count = 0      
        self.dfs(root, 0, {0: 1}, target)
        
        return self.count

    def dfs(self, root, psum, psum_to_freq, target):
        if not root:
            return 
        
        psum += root.val
        if psum - target in psum_to_freq:
            self.count += psum_to_freq[psum - target]
    
        psum_to_freq[psum] = psum_to_freq.get(psum, 0) + 1

        self.dfs(root.left, psum, psum_to_freq, target)
        self.dfs(root.right, psum, psum_to_freq, target)

        psum_to_freq[psum] -= 1 


# top-down
class Solution(object):
    def pathSum(self, root, target):
        psum_to_freq = {0:1}
        return self.dfs(root, 0, target, psum_to_freq)

    def dfs(self, root, psum, target, psum_to_freq):
        if not root:
            return 0

        res = 0
        psum += root.val
        if psum - target in psum_to_freq:
            res += psum_to_freq[psum - target]
        
        psum_to_freq[psum] = psum_to_freq.get(psum, 0) + 1

        res += self.dfs(root.left, psum, target, psum_to_freq)
        res += self.dfs(root.right, psum, target, psum_to_freq)

        psum_to_freq[psum] -= 1

        return res


#****************************************** traverse ***************************************************    
# 257. Binary Tree Paths - all solutions
class Solution:
    def binaryTreePaths(root):
        if root is None:
            return []
        
        res = []
        self.dfs(root, [str(root.val)], res)
        return res
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, res)      # backtrack 
            path.pop() 
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, res)
            path.pop()   
            
 
# 113. Binary Tree Path Sum - all solutions
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        self.dfs(root, target, [], res)
        
        return res
    
    def dfs(self, node, target, path, res):
        if not node:
            return 
            
        if target == node.val and node.left is None and node.right is None:
            res.append(list(path + [node.val]))
            return
            
        path.append(node.val)
        self.dfs(node.left, target - node.val, path, res)
        self.dfs(node.right, target - node.val, path, res)    # backtrack
        path.pop()
        

# 272. K Closest BST Values 
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


# 102. Binary Tree Level Order Traversal - bfs
def levelOrder(root):
    if root is None:
        return []
        
    queue = deque([root])
    res = []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
        
    return res


# 297. Serialize and Deserialize Binary Tree - bfs
#                                            - dfs

class Codec:
    def serialize(self, root):
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


    def deserialize(self, data):

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
                res.append("#")
                return 
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        def helper(queue):
            if queue[0] == "#":
                queue.popleft()
                return
            root = TreeNode(queue.popleft())
            l = helper(queue)
            r = helper(queue)
            root.left = l
            root.right = r
            return root
        
        tree = data.split(",")
        queue = collections.deque(tree)
        return helper(queue)
    
