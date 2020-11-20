"""
# d&q
# LCA in BST - iteration O(logn)
# LCA in Binary Tree - d&q O(n) O(n)(recursion stack)
# LCA in Binary Tree - node may not exist - d&q


# traverse recursion
# K Closest Values in a BST - inorder O(n)
# All nodes Distance K in a Binary Tree - preorder O(n)


# BST iterator
# K Smallest Values in a BST - O(k)
# K Closest Values in a BST - O(logn + k)

"""


#************************************************** LCA ***************************************************
# LCA in BST
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

  
# LCA in Binary Tree
"""""""""
(3,5) -> 4

            4 (4)
           / \
      (3) 3   7 (5)
             / \
        (5) 5   6(None)
        
"""""""""
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
  
 
# LCA in Binary Tree - node may not exist
"""""""""
(3,9) -> None

                      4 (T, F, 3) -> None
                     / \
          (T, F, 3) 3   7 (F, F, None)
                       / \
         (F, F, None) 5   6(F, F, None)
        
"""""""""
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


  



# Invert a Binary Tree
def invertTree(root):
    if not root:
        return
    
    self.invertTree(root.left)
    self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    
    return root
