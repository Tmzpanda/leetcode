
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



# 257. Binary Tree Paths - all solutions
class Solution:
    def binaryTreePaths(root):
        if root is None:
            return []
        
        res = []
        self.dfs(root, [str(root.val)], res)
        return res
    
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, res)      # backtrack 
            path.pop() 
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, res)
            path.pop()   
            
