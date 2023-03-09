# 622. Design Circular Queue

class Node: 
    def __init__(self, idx, value):
        self.idx = idx
        self.val = value
        self.next = None
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = self.tail = None
        self.idx_to_prev = {}          # idx_to_prev   # search   
        self.size = 0
        self.capacity = k
        

    def enQueue(self, val: int) -> bool:
        if self.size >= self.capacity:
            return False
        
        if self.size == 0:
            node = Node(0, val)
            self.head = self.tail = node
        else:
            node = Node(self.tail.idx + 1, val)
            self.idx_to_prev[node.idx] = self.tail
            self.tail.next = node
            self.tail = node
            
        self.size += 1
        return True
        
        
    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        # next
        del self.idx_to_prev[self.head.next.idx]
        self.head = self.head.next
        
        self.size -= 1
        return True
        

    def Front(self) -> int:
        return self.head.val
        

    def Rear(self) -> int:
        return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        

        
        
        
class CircularArray:
    def __init__(self):
        self.array = [0] * 10
        self.start = self.end = 0
        self.size = 0
        
    def append(self, val):
        if self.size == 0:
            self.array[self.start] = val
            self.size = 1
            return 
        
        if self.size == len(self.array):
            self.extend()
        
        self.end = get_index(end + 1)
        self.array[self.end] = val
        self.size += 1
        
    def appendleft(self, val):
        if self.size == 0:
            self.array[self.start] = val
            self.size = 1
            return 
        
        if self.size == len(self.array):
            self.extend()
            
        self.start = self.get_index(self.start - 1)
        self.array[self.start] = val
        self.size += 1
        
    def pop(self):
        res = self.array[self.end]
        if self.size != 1:
            end = self.get_index(self.tail - 1)
        
        self.size -= 1
        return res
    
    def popleft(self):
        res = self.array[self.start]
        if self.size != 1:
            end = self.get_index(self.start + 1)
        
        self.size -= 1
        return res 
    
    def get(self, index):
        return self.array[self.start + index]
    
    def put(self, index, value):
        self.array[self.start + index] = value
        
    def get_index(self, index):
        return (index + len(self.array)) % len(self.array)
    
    def extend(self):
        self.array2 = [0] * len(self.array) * 2
        for i in range(len(self.array)):
            self.array2[i] = self.array[(self.start + i) % len(self.array)]
        
        self.start, self.end = 0, len(self.array) - 1
        self.array = self.array2 
    
    def get_index(self, index):
        return (index + len(self.array)) % len(self.array)
