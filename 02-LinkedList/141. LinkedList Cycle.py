# 141. LinkedList Cycle
def hasCycle(head):
    if head is None:            
        return False    
    
    p1 = head.next       # 2 pointers
    p2 = head       
    while p1 != p2:
        if p1 is None or p1.next is None:
            return False
        
        p1 = p1.next.next
        p2 = p2.next
    
    return True