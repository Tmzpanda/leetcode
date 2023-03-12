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