"""
# dummy node
# merge


# pointers
# hasCycle
# middleNode
# Remove Nth Node from the end - one pass
# reverse 
          


# data structure
# LRU
# First Unique Number in Data Stream


"""

#********************************* dummy node **********************************************
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
    
 

#********************************* pointers **********************************************
# hasCycle
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


# middle node
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


# Remove Nth Node from the end - one pass
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



# reverse
# 3 pointers
"""
prev cur next
      1 -> 2 -> 3 -> None
     
"""
def reverse(head):
    prev = None
    while head:
        nxt = head.next

        head.next = prev
        prev = head
        head = nxt

    return prev



    




#********************************* data structure **********************************************
# LRU
"""
                  tail
dummy <- 1 <- 2 <- 3

set - if exists - pop and append
    - if not - append, popleft
    
get - if exists - pop and append
    - if not - return -1
    
"""
class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:
    def __init__(self, capacity):
        self.key_to_prev = {}           # key_to_prev
        self.dummy = Node()
        self.tail = self.dummy
        self.capacity = capacity

    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        self.pop(self.key_to_prev[key].next) 
        return self.key_to_prev[key].next.value 

    def set(self, key, value):
        if key in self.key_to_prev:
            self.pop(self.key_to_prev[key].next) 
            self.key_to_prev[key].next.value = value
            
        else:
            self.append(Node(key, value))
            if len(self.key_to_prev) > self.capacity:
                self.popleft()
        
    def pop(self, node):
        if node == self.tail:
            return
        
        # prev
        prev = self.key_to_prev[node.key]
        prev.next = node.next
        # next
        self.key_to_prev[node.next.key] = prev
        # curr
        self.append(node)
        
    def append(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
     
    def popleft(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy



# First Unique Number in Data Stream 
"""
                  tail
dummy <- 1 <- 2 <- 3

add - first time - append
    - second time - pop, duplicate
    - third time - return 

"""
class DataStream:
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()

    def add(self, num):
        if num in self.duplicates:
            return 
        
        if num in self.num_to_prev:
            self.pop(num)
            self.duplicates.add(num)
        else: 
            self.append(num)

    def firstUnique(self):
        if not self.dummy.next:
            return None
        return self.dummy.next.val
        
    def pop(self, num):
        # prev
        prev = self.num_to_prev[num]
        prev.next = prev.next.next
        # curr
        del self.num_to_prev[num]  
        # next
        if prev.next:
            self.num_to_prev[prev.next.val] = prev
        else:
            self.tail = prev
            
    def append(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next

    


















