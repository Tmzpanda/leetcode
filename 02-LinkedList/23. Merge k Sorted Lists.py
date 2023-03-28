# 23. Merge k Sorted Lists 
# O(nlogk)
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # base
    if len(lists) == 1:
            return lists[0]
        
    # divide and conquer
    mid = len(lists) // 2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])
    
    return merge(left, right)
    
    
def merge(l1: ListNode, l2: ListNode) -> ListNode:
    cur = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l1.val:
            cur.next = l1
            l1 = p1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
        
    cur.next = p1 or p2
   
    return dummy.next 
