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

