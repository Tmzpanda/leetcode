"""
# K Smallest 
# K Largest


# K Closest - recursion
            - iteration 
            

"""

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
