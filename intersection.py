"""
# intersection of two sorted array  - two pointers O(m + n)    - m ≈ n
                                    - binary search O(m.logn)  - m ≫ n
                                    
# intersection of two BST  - recursion  O(m + n)    - m ≈ n
                           - iteration  O(m + n)    - m ≫ n       
                           
# intersection of two Linked List 
# merge two Linked List 



"""
#********************************* intersection of two sorted array **********************************************
# two pointers O(m + n) 
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    res = []

    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res
    
    
# binary search O(m.logn) 
def intersection(arr1, arr2):
    result = []
    
    for num in arr1:
        if binarySearchFound(arr2, num):
            result.append(num)
    return result

def binarySearchFound(nums, target):
    l, r = 0, len(nums) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif target < nums[mid]:
            r = mid
        else:
            l = mid

    if nums[l] == target:
        return True
    if nums[r] == target:
        return True
    return False

    
#********************************* intersection of two BST **********************************************
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
        self.getStack(stack1, root1)
        self.getStack(stack2, root2)
        
        res = []
        while stack1 and stack2:
            if stack1[-1].val < stack2[-1].val:
                node = stack1.pop()
                self.getStack(stack1, node.right)
            elif stack1[-1].val > stack2[-1].val:
                node = stack2.pop()
                self.getStack(stack2, node.right)
            else:
                node = stack1.pop()
                self.getStack(stack1, node.right)
                res.append(node.val)
                      
        return res

    def getStack(self, stack, root):
        while root:
            stack.append(root)
            root = root.left


#********************************* two LinkedList **********************************************
# intersection 
def intersection(l1, l2):      
    res = []
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val < p2.val:
            p1 = p1.next
        elif p1.val > p2.val:
            p2 = p2.next
        else:
            res.append(p1.val)
            p1 = p1.next
            p2 = p2.next
        
    return res
  
  
# merge
def merge(l1, l2): 
    temp = dummy = ListNode(0)
    p1, p2 = l1, l2
    while p1 or p2:
        if isFirstPointerSmaller(p1, p2):
            temp.next = p1
            p1 = p1.next
        else:
            temp.next = p2
            p2 = p2.next
        temp = temp.next

    return dummy.next

def isFirstSmaller(p1, p2):
    if p1 is None:
        return False
    if p2 is None:
        return True
    return p1.val <= p2.val



