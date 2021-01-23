

#******************************************************** quick select *************************************************************     




#***************************************************** LCA in a BST *************************************************************
# iteration
def lowestCommonAncestorInBST(root, p, q):
    node = root
    while node:
        if p.val > node.val and q.val > node.val:
            node = node.right
        elif p.val < root.val and q.val < root.val:
            node = node.left
        else:
            return node
    
    return None


# recursion
def lowestCommonAncestorInBST(root, p, q):
    if not root:
        return None

    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestorInBST(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestorInBST(root.left, p, q)
    else:
        return root








