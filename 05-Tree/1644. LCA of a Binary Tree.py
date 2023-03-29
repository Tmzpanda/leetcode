# 1644. Lowest Common Ancestor of a Binary Tree II - node may not exist
"""
                      4 (T, F, None)
                     / \
       (T, F, None) 3   7 (F, F, None)
                       / \
         (F, F, None) 5   6 (F, F, None)

(3,9) -> None

"""
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    def dfs(root):
        # base
        if root is None:
            return False, False, None
        # d&q
        left_found_p, left_found_q, left_lca = dfs(root.left)     # return lca
        right_found_p, right_found_q, right_lca = dfs(root.right)
        
        # combine
        found_p = left_found_p or right_found_p or root == p
        found_q = left_found_q or right_found_q or root == q
        lca = None
        
        if left_lca is not None:
            lca = left_lca
        elif right_lca is not None:
            lca = right_lca
        elif found_p and found_q:
            lca = root
            
        return found_p, found_q, lca
      
    _, _, lca = dfs(root)
    return lca
      
    
  
  
  
  

