# 236. LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
"""
(3,5) -> 4

            4 (4)
           / \
      (3) 3   7 (5)
             / \
        (5) 5   6(None)
        
"""
def lowestCommonAncestor(root, A, B): 
    if root is None:
        return None
        
    if root is A or root is B:                      
        return root
        
    left = self.lowestCommonAncestor(root.left, A, B)   
    right = self.lowestCommonAncestor(root.right, A, B)
    
    if left is not None and right is not None:     
        return root
    if left is not None:                            
        return left
    if right is not None:                        
        return right
    
    return None  
  