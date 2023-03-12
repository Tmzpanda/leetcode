
# 23. Merge k Sorted Lists - O(Nlogn), where n is # of LinkedLists, N is # of nodes
def mergeNLists(lists):
    return mergeRange(lists, 0, len(lists) - 1)

def mergeRange(lists, start, end):
    if start == end:
        return lists[start]

    mid = (start + end) // 2
    left = mergeRange(lists, start, mid)
    right = mergeRange(lists, mid + 1, end)
    return merge(left, right)
    
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

