# 206. Reverse LinkedList
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
