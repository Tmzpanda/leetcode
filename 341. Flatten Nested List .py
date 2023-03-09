# 341. Flatten Nested List 

# batch
def flatten(nestedList):
    res = []
    for item in nestedList:
        if isinstance(item, list):
            res.extend(flatten(item)) # recursion
        else:
            res.append(item)

    return res
  
  
# Iterator 
class NestedIterator:
    def __init__(self, nestedList):
        self.queue = deque(nestedList)
        self.next_int = None

    def next(self) -> int:
        return self.next_int

    def hasNext(self) -> bool:
        while self.queue:
            next_item = self.queue.popleft()
            if isinstance(next_item, int):
                self.next_int = next_item
                return True
              
            else:
                next_list = next_item
                while next_list:
                    self.queue.appendleft(next_list.pop())

        return False
      
res = []
iterator = NestedIterator(nestedList)
while iterator.hasNext(): 
    res.append(iterator.next())
    
    
  
