# delete
def delete_node(root, val):

    def find_smallest(root):
        while root.left:
            root = root.left
        return root

    if not root:
        return

    if root.val > val:
        root.left = delete_node(root.left, val)
    elif root.val < val:
        root.right = delete_node(root.right, val)

    else:
        #  No Child or One Child
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        # Two children - Find min node in right subtree, copy the value, then delete min node from right subtree
        else:
            temp = find_smallest(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)

    return root
