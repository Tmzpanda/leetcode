

#******************************************************** quick select *************************************************************     
# recursion top-down with return
def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        return partition(nums, start, r, k)
    if k >= l:
        return partition(nums, l, end, k)
        
    return nums[k]


# recursion top-down
def kthSmallest(nums, k):
    partition(nums, 0, len(nums - 1), k - 1)

    return nums[k - 1]


def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        partition(nums, start, r, k)
    if k >= l:
        partition(nums, l, end, k)





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








