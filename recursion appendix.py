
"""
        bottom-up                                                               top-down
        
                        A. if directed, then alternative - LIS 1d vs Longest Increasing Subarray 2d 
        1. dp          <---------------------------------------------------->  
                                                                                1. dfs memoization
                        B. dfs all solutions - Word Ladder vs Word Break                
        2. backtrack   <---------------------------------------------------->       
        
        
                |                                                                      |       
                |                                                                      |
                |                                                                      |
                |                                                                      |
                | C. traverse + take or not                                            | D. divide conquer - no duplicate sub-problems
                |    Binary Tree Paths                                                 |       
                |                                                                      |
                |                                                                      |
                |                                                                      |
                |                                                                      |
                ↓        E. tree - depth vs height                                     ↓       
        3. traverse     <---------------------------------------------------->   2. divide conquer       
       



     
A.                
                                 LIS 1d - directed
   bottom-up                                             top-down
   dp: set i, update j (according to i)        dfs memoization: update j (according to i)
                                                                1. branches, duplicate sub-problems
                                                                2. reduce to subproblem, return



                                                         A.1    Longest Increasing Subarry 2d - no direction
                                                                dfs memoization:  ------------------------------------> dp? sort - brings direction
                                                                1. branches and duplicate sub ✓
                                                                2. reduce and return ✓
                                                                
                                                         A.2    Insert Star
                                                                dfs
                                                                1. branches and duplicatee sub x
                                                                2. reduce and return ✓
   
   
   
   dp  <------------------------> dfs memoization
 initialization                  break condition
 bottom-up                       top-down
 return                          return
                                                                
                                                                
 
 
 
 
# recursion with/without return 
# insert star - iteration
              - recursion bottom-up with return
              - recursion bottom-up

# quick select - recursion top-down with return
               - recursion top-down

# binary search - iteration
                - recursion top-down with return
                
# LCA in a BST - iteration
               - recursion
               
                
                



# string vs array with index
# array with index - (nums, start, end) - quick sort
                                        - combination sum
# string - (s[i:]) - insert star
                   - word break
                   - merge sort


"""
#********************************* insert star ****************************************
# insert star
# iteration
def insertStar(string):
    output = ""
    for i in range(len(string)):
        if i > 0 and string[i] != string[i - 1]:
            output += '*' + string[i]
        else:
            output +=  string[i]
    
    return output


# recursion bottom-up with return
def insertStar(string):
    return rec(string, 0, "")

def rec(string, index, temp):
    if index == len(string):
        return temp

    if index > 0 and string[index] != string[index - 1]:
        temp += '*'
    temp += string[index]

    return rec(string, index + 1, temp)


# recursion bottom-up 
def insertStar(string):
    result =  []
    rec(string, 0, result)
    return "".join(result)
    
def rec(string, index, result):
    if index == len(string):
        return 
    
    if index > 0 and string[index] != string[index - 1]:
        result.append('*')
        
    result.append(string[index])
    rec(string, index + 1, result)


#********************************* quick select ****************************************     
# recursion top-down with return
def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        return partition(nums, start, r, k)
    if k >= l:
        return partition(nums, l, end, k)
        
    return nums[k]


# recursion top-down
def kthSmallest(nums, k):
    partition(nums, 0, len(nums - 1), k - 1)

    return nums[k - 1]


def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        partition(nums, start, r, k)
    if k >= l:
        partition(nums, l, end, k)



#********************************* binary search ****************************************
# iteration
def binary_search(nums, target):
    l, r = 0, len(nums) - 1


    while l + 1 < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid
        else:
            r = mid

    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1


# recursion
def binary_search(nums, target):
    return dfs(nums, 0, len(nums) - 1, target)

def dfs(nums, start, end, target):
    if start + 1 == end:
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return dfs(nums, mid, end, target)
    else:
        return dfs(nums, start, mid, target)


#********************************* LCA in a BST ****************************************
# iteration
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


# recursion
def lowestCommonAncestorInBST(root, p, q):
    if not root:
        return None

    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestorInBST(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestorInBST(root.left, p, q)
    else:
        return root







