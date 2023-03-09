# 108. Convert Sorted Array to Binary Search Tree 

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
