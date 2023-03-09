
# 145. Binary Tree Postorder Traversal

# recursion
def postorder_traverse(root):      

    def rec(node, res):
        if node is None:
            return
        
        rec(node.left, res)
        rec(node.right, res)
        res.append(node.val)

        # return

    res = []
    rec(root, res)
    return res

# iteration
def postorder_traverse(root):

    res = deque()
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node:
            res.appendleft(curr_node.val)   # appendleft
            stack.append(curr_node.left)
            stack.append(curr_node.right)

    return res
