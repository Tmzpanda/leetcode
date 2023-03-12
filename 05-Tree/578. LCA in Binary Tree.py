# 578. LCA in Binary Tree - may not exist - d&q O(n) O(n)
"""
(3,9) -> None

                      4 (T, F, 3) -> None
                     / \
          (T, F, 3) 3   7 (F, F, None)
                       / \
         (F, F, None) 5   6(F, F, None)
        
"""
class Solution:

    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B) 

        if a and b:                                         
            return lca
        else:
            return None

    def helper(self, root, A, B):
        if root is None:
            return False, False, None
            
        leftA, leftB, left = self.helper(root.left, A, B)
        rightA, rightB, right = self.helper(root.right, A, B)
        
        a = leftA or rightA or root == A
        b = leftB or rightB or root == B
        
        if root is A or root is B:                           
            return a, b, root
            
        if left and right:
            return a, b, root
        if left:                        
            return a, b, left
        if right:                 
            return a, b, right

        return a, b, None 