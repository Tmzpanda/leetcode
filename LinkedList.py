"""
# dummy node
# merge


# 2 pointers
# hasCycle
# middleNode


# node_to_prev
# reverse - hashmap O(n) O(n)
          - pointers O(n) O(1)


# data structure
# LRU
# Data Stream


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
    
 

#********************************* 2 pointers **********************************************
# hasCycle
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



#********************************* node_to_prev **********************************************
# reverse
# hashmap
"""
 o -> o -> o -> o -> None
 ^
                ^
"""
def reverseList(head):
    if not head:
        return None
    
    node_to_prev = {head: None}
    while head.next:
        node_to_prev[head.next] = head
        head = head.next
    
    for node in node_to_prev:
        node.next = node_to_prev[node]
        
    return head


# 3 pointers
"""
     o -> o -> o -> o -> None
 p   ^        
                    p     ^          
"""
def reverse(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev

        prev = head
        head = temp

    return prev



#********************************* data structure **********************************************
# LRU
"""
      x - o1 - o - o - o 
          -
          
      x - o - o - o - o1    key_to_prev
      -   -           -        -


set - if exists - pop and append
    - if not - append, *popleft
    
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
        self.key_to_prev = {} 
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
        node.next = None
        
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
      x - o1 - o - o - o   o1    o1   o1
          -                2     3    4
          
      x - o - o - o     key_to_prev      duplicates
      -   -                 -                -


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

    


















