"""
dummy 
# 21. Merge Two Sorted Lists


pointers
# 141. LinkedList Cycle
# 876. LinkedList Middle
# 19. Remove Nth Node from the end - one pass
# 206. Reverse LinkedList
# 160. Intersection of Two Linked Lists  

"""

#********************************* dummy node **********************************************
# 21. Merge Two Sorted Lists
def merge(l1, l2):

    temp = dummy = ListNode(0)
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val <= p2.val:
            temp.next = p1
            p1 = p1.next
        else:
            temp.next = p2
            p2 = p2.next
        temp = temp.next
        
    temp.next = p1 or p2
    
    return dummy.next 
    
 

#********************************* pointers **********************************************
# 141. LinkedList Cycle
# 2 pointers
def hasCycle(head):
    if head is None:            
        return False    
    
    p1 = head.next       
    p2 = head       
    while p1 != p2:
        if p1 is None or p1.next is None:
            return False
        
        p1 = p1.next.next
        p2 = p2.next
    
    return True


# 876. LinkedList Middle
"""
 1 -> 2 -> 3 -> 4
           f
      s
"""
def middleNode(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# 19. Remove Nth Node from the end - one pass
"""
 dummy -> 1 -> 2 -> 3 -> 4              n = 2
                         f          
               s
"""

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    for _ in range(n):
        fast = fast.next   
        
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    
    return dummy.next



# 206. Reverse LinkedList
# 3 pointers
"""
prev cur next
      1 -> 2 -> 3 -> None
     
"""
def reverse(head):
    prev = None
    while head:
        next = head.next

        head.next = prev
        prev = head
        head = next

    return prev



# 160. Intersection of Two Linked Lists   
def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    p1, p2 = headA, headB
    while p1 != p2:
        if p1 is None:
            p1 = headB
        else:
            p1 = p1.next
        
        if p2 is None:
            p2 = headA
        else:
            p2 = p2.next
            
    return p1










