# 236. LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
"""
            4 (4)
           / \
      (3) 3   7 (5)
             / \
        (5) 5   6 (None)

(3,5) -> 4

"""
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root):
        # base
        if root is None or root == p or root == q:
            return root
    
        l = dfs(root.left)     # return lca, or p or q        
        r = dfs(root.right)
        
        if l and r:
            return root
        else:
            return l or r

    return dfs(root)

            
   
