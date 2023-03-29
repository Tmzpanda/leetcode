# 1676. Lowest Common Ancestor of a Binary Tree IV
def lowestCommonAncestor(root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
    nodes = set(nodes)

    def dfs(root):
        if not root:
            return None
        if root in nodes:
            return root

        l = dfs(root.left)
        r = dfs(root.right)
        if l and r:
            return root
        else:
            return l or r

    return dfs(root)
