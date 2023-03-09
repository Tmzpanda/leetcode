# 701. Insert into a Binary Search Tree


# insert
def insert_node(root, val):
    if not root:
        return TreeNode(val)
    if root.val > val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root
