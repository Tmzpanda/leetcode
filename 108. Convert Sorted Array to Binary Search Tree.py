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





# use this d&q problem to see how break condition can be reconcilidate in tree recursion problems

from Tree import TreeNode
from Tree import inorder_traverse


# intuitive solution
def sortedArrayToBST(nums) -> TreeNode:

    def rec(nums, l, r) -> TreeNode:
        if l > r:
            return None

        if l == r:      
            root = TreeNode(nums[l])
            root.left, root.right = None, None

        else:
            mid = (l+r) // 2   
            root = TreeNode(nums[mid])
            root.left, root.right = rec(nums, l, mid-1),  rec(nums, mid+1, r)

        return root

    if not nums:
        return 
    
    l, r = 0, len(nums) - 1
    mid = (l + r) // 2
    root = TreeNode(nums[mid])
    root.left, root.right = rec(nums, 0, mid-1), rec(nums, mid+1, len(nums)-1)


    return root


# reconciliation 
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

