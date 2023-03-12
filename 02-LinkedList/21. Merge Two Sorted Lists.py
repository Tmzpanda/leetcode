# 21. Merge Two Sorted Lists
def merge(l1, l2):

    temp = dummy = ListNode(0) # dummy node
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