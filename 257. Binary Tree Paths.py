
# all paths
# https://leetcode.com/problems/binary-tree-paths/description/
def binaryTreePaths(root):

    def dfs(root, path, res):
        if root.left is None and root.right is None:
            res.append(list(path))
            return

        for node in (root.left, root.right):
            if node:
                path.append(str(node.val))
                dfs(node, path, res)
                path.pop()

    path = [str(root.val)]
    res = []
    dfs(root, path, res)

    return ['->'.join(path) for path in res]
