
# 145. Binary Tree Postorder Traversal

# recursion
def postorderTraversal(self, root: TreeNode) -> List[int]:    
    def dfs(node):
        if node is None:
            return
        
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    res = []
    dfs(root)
    return res
