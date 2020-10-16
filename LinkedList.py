"""
# merge
# hasCycle
# middleNode

"""



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
    
 
# hasCycle
def hasCycle(head):
    if head is None:            
        return False    
    
    p1 = head       
    p2 = head       
    while p1 != p2:
        if p1 is None or p1.next is None:
            return False
        
        p1 = p1.next.next
        p2 = p2.next
    
    return True
