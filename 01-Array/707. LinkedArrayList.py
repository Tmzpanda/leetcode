# 707. LinkedArrayList 
"""
 head                      tail
 -2 <- -1 <- 0 <- 1 <- 2 <- 3
             ^

"""
class Node: 
    def __init__(self, idx, value):
        self.idx = idx
        self.val = value
        self.next = None
        
        
class LinkedArrayList:
    def __init__(self):
        self.head = self.tail = None
        self.idx_to_prev = {}          # idx_to_prev   # search   
        self.size = 0
    
    def append(self, val):
        if self.size == 0:
            node = Node(0, val)
            self.head = self.tail = node
        else:
            node = Node(self.tail.idx + 1, val)
            self.idx_to_prev[node.idx] = self.tail
            self.tail.next = node
            self.tail = node
            
        self.size += 1

    def appendleft(self, val):
        if self.size == 0:
            node = Node(0, val)
            self.head = self.tail = node
        else:
            node = Node(self.head.idx - 1, val)
            self.idx_to_prev[self.head.idx] = node
            node.next = self.head
            self.head = node
        
        self.size += 1
        
    def pop(self):                         
        # prev
        prev = self.idx_to_prev[self.tail.idx]
        prev.next = None
        # curr
        res = self.tail.val
        del self.idx_to_prev[self.tail.idx]
        # next
        self.tail = prev
        
        self.size -= 1
        return res
        
    def popleft(self):      # O(1)
        # curr
        res = self.head.val
        # next
        del self.idx_to_prev[self.head.next.idx]
        self.head = self.head.next
        
        self.size -= 1
        return res
    
    def get(self, index):   # O(1)
        if index == 0:
            return self.head.value       
        return self.idx_to_prev[self.head.idx + index].next.val
    
    def put(self, index, value):    
        if index == 0:
            self.head.val = value
        else:
            self.idx_to_prev[self.head.idx + index].next.val = value
        
        
# test case
def print_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print('->'.join(result))
    
ll = LinkedArrayList()
ll.append(2)
ll.append(3)
ll.append(4)
ll.appendleft(1)
print_list(ll.head)
print(ll.pop())
print(ll.popleft())
ll.put(1, 30)
print(ll.get(0))
print(ll.get(1))
print_list(ll.head)

