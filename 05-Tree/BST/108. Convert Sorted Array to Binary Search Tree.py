# 108. Convert Sorted Array to Binary Search Tree
# divide and conquer
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    # base
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root
    

# another way
def sortedArrayToBST(nums: List[int]) -> TreeNode:
    def dfs(l, r):  
        # base
        if l > r:
            return None
        # d&q
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = dfs(l, mid - 1)     # using indices avoids creating new subarrays in each recursion
        root.right = dfs(mid + 1, r)
        
        return root
       
    return dfs(0, len(nums) - 1)

