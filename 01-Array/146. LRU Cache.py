# 146. LRU Cache
"""
                  tail
dummy <- 1 <- 2 <- 3


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
        self.dummy = Node()
        self.tail = self.dummy
        self.key_to_prev = {}           # key_to_prev 
        self.capacity = capacity

    def get(self, key):
        if key not in self.key_to_prev:
            return -1
        
        self.pop(self.key_to_prev[key].next) 
        return self.key_to_prev[key].next.value 

    def put(self, key, value):
        if key in self.key_to_prev:
            self.pop(self.key_to_prev[key].next) 
            self.key_to_prev[key].next.value = value
            
        else:
            self.append(Node(key, value))
            if len(self.key_to_prev) > self.capacity:
                self.popleft()
  

    def append(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop(self, node):
        if node == self.tail:
            return
        
        # prev
        prev = self.key_to_prev[node.key]
        prev.next = node.next
        # current
        del self.key_to_prev[node.key]  
        # next
        self.key_to_prev[node.next.key] = prev
      
        self.append(node)
        
    def popleft(self):
        node = self.dummy.next
        # prev
        self.dummy.next = node.next
        # current
        del self.key_to_prev[node.key]
        # next
        self.key_to_prev[node.next.key] = self.dummy
    