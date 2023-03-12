# 230. Kth Smallest Element in a BST - iterator O(k)
def kthSmallest(root, k):
    stack = []
    node = root
    while node:     
        stack.append(node)
        node = node.left
        
    for i in range(k):
        node = stack.pop()
        res = node.val
        
        node = node.right
        while node:        
            stack.append(node)
            node = node.left
            
    return res