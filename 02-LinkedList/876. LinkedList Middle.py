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