# 144. Binary Tree Preorder Traversal

# recursion
def preorderTraversal(root: TreeNode) -> List[int]:
    def dfs(node):
        if node is None:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)

    res = []
    dfs(root)
    return res

  
# iteration
def preorderTraversal(root: TreeNode) -> List[int]:
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        
    return res
