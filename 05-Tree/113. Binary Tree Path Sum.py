            
# 113. Binary Tree Path Sum - all solutions
class Solution:
    def pathSum(self, root, target):
        res = []
        self.dfs(root, target - root.val, [root.val], res)
        
        return res
    
    def dfs(self, node, target, path, res):
        if target == 0 and not node.left and not node.right:
            res.append(list(path))
            return
        
        # dfs
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, target - node.left.val, path, res)      
            path.pop() 
        
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, target - node.right.val, path, res)
            path.pop()  



# a second bottom-up
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
        
        # dfs  
        path.append(node.val)
        self.dfs(node.left, target - node.val, path, res)
        self.dfs(node.right, target - node.val, path, res)
        path.pop()       

     