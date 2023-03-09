# https://github.com/Tmzpanda/leetcode-basics/blob/master/tree/bst.py

from Tree import TreeNode
from Tree import inorder_traverse

# BST-ify 
def sortedArrayToBST(nums):

    def rec(nums, l, r):
        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = rec(nums, l, mid - 1)
        root.right = rec(nums, mid + 1, r)

        return root

    return rec(nums, 0, len(nums) - 1)

nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
res = inorder_traverse(root)
print(res)


# insert
def insert_node(root, val):
    if not root:
        return TreeNode(val)
    if root.val > val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root


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


# search


# Iterator
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        node = self.stack.pop()
        res = node

        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left

        return res
