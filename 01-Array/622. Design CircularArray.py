# 622. Design CircularArray
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
        
        self.end = self.get_index(self.end + 1)
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
            self.end = self.get_index(self.end - 1)
        
        self.size -= 1
        return res
    
    def popleft(self):                             # O(1)
        res = self.array[self.start]
        if self.size != 1:
            self.start = self.get_index(self.start + 1)
        
        self.size -= 1
        return res 
    
    def get(self, index):                          # O(1)
        return self.array[self.get_index(self.start + index)]
    
    def put(self, index, value):
        self.array[self.get_index(self.start + index)] = value
       
    def get_index(self, index):
        return (index + len(self.array)) % len(self.array)
    
    def extend(self):
        self.array2 = [0] * len(self.array) * 2
        for i in range(len(self.array)):
            self.array2[i] = self.array[get_index(self.start + i)]
        
        self.start, self.end = 0, len(self.array) - 1
        self.array = self.array2 

# test
ca = CircularArray()
ca.append(2)
ca.append(3)
ca.append(4)
ca.appendleft(1)
print(ca.get(1))
print(ca.array, ca.start, ca.end)
ca.pop()
print(ca.array, ca.start, ca.end)
ca.popleft()
print(ca.array, ca.start, ca.end)
print(ca.get(1))
ca.put(1, 30)
ca.get(1)
