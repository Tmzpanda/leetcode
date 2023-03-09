# 144. Binary Tree Preorder Traversal

# recursion
from collections import deque


def preorder_traverse(root):

    def rec(node, res):
        if node is None:
            return

        res.append(node.val)
        rec(node.left, res)
        rec(node.right, res)

    res = []
    rec(root, res)
    return res

  
# iteration
def preorder_traverse(root):

    res = []
    stack = [root]
    while stack:
        curr_node = stack.pop()
        if curr_node:
            res.append(curr_node.val)
            stack.append(curr_node.right)
            stack.append(curr_node.left)
        
    return res
