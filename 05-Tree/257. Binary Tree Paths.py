# 257. Binary Tree Paths

def binaryTreePaths(root: TreeNode) -> List[str]:
    def dfs(node, path):
        if not node.left and not node.right:
            res.append(list(path))
            return

        for node in (node.left, node.right):
            if node:
                path.append(str(node.val))
                dfs(node, path)
                path.pop()       # backtrack

    res = []
    dfs(root, [str(root.val)])

    return ['->'.join(path) for path in res]
