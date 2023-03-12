# 270. Closest BST Value - binary search O(logn)
def closestValue(root, target):
    p1, p2 = None, None
  
    node = root
    while node:
        if target > node.val:
            p1 = node
            node = node.right
        elif target < node.val:
            p2 = node
            node = node.left
        else:
            return node.val
 
    return min(p1.val, p2.val, key=lambda x: abs(x - target))
