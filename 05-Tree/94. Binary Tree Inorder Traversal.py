# 94. Binary Tree Inorder Traversal 


# inorder
# recursion
def inorder_traverse(root):    
    
    def rec(node, res):
        if node is None:
            return

        rec(node.left, res)
        res.append(node.val)
        rec(node.right, res)

        # return

    res = []    # closure
    rec(root, res) 
    return res

# iteration
def inorder_traverse(root):

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

