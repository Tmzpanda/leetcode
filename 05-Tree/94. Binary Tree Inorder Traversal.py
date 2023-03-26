# 94. Binary Tree Inorder Traversal 

# recursion
def inorderTraversal(root: TreeNode) -> List[int]: 
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    res = []    
    dfs(root) 
    return res


# iteration
def inorderTraversal(root: TreeNode) -> List[int]: 

    res = []
    stack = []
    # initialize
    while root:
        stack.append(root)
        root = root.left

    # stack
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left

    return res

