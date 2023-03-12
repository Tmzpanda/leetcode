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