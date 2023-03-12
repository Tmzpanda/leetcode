"""
# 000. Intersection of two BST - m ≈ n - recursion merge O(m + n)   
                                       - iteration merge O(m + n)    
                               - m ≫ n - binary search O(n.logm)
                          



"""

# Intersection of two BST 
# recursion O(m + n)  
class Solution:
    def intersection(self, root1, root2):
        arr1, arr2 = [], []
        self.traverse(root1, arr1)
        self.traverse(root2, arr2)
        
        # merge
        i, j = 0, 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                result.append(arr1[i])
                i += 1
                j += 1
                
        return result
    
    def traverse(self, root, arr):
        if not root:
            return
        self.traverse(root.left, arr)
        arr.append(root.val)
        self.traverse(root.right, arr)

        
# iteration O(m + n)  
class Solution:
    def intersection(self, root1, root2):
        stack1, stack2 = [], []
        self.getSuccessor(stack1, root1)
        self.getSuccessor(stack2, root2)
        
        res = []
        while stack1 and stack2:
            if stack1[-1].val < stack2[-1].val:
                node = stack1.pop()
                self.getSuccessor(stack1, node.right)
            elif stack1[-1].val > stack2[-1].val:
                node = stack2.pop()
                self.getSuccessor(stack2, node.right)
            else:
                node = stack1.pop()
                self.getSuccessor(stack1, node.right)
                res.append(node.val)
                      
        return res

    def getSuccessor(self, stack, root):
        while root:
            stack.append(root)
            root = root.left
            
            