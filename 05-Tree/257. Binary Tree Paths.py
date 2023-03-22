# 257. Binary Tree Paths

def binaryTreePaths(root):

    def dfs(root, path, res):
        if not root.left and not root.right:
            res.append(list(path))
            return

        for node in (root.left, root.right):
            if node:
                path.append(str(node.val))
                dfs(node, path, res)
                path.pop()       # backtrack

    res = []
    dfs(root, [str(root.val)], res)

    return ['->'.join(path) for path in res]
