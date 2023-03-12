# 685. First Unique Number - Data Stream 
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
    
    def append(self, num):
        node = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail.next = node
        self.tail = node
        
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
            
    