"""
# data structure
# First Unique 

# stats
# Moving Average
# Median

"""
#************************************************ Data Structure ************************************
# Fisrt Unique Number - batch
def firstUniqueNumber(nums):
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    for num in nums:
        if counter[num] == 1:
            return num
        
    return -1


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


#************************************************ stats **********************************************
# Moving Average
class MovingAverage:
    
    def __init__(self, size):
        self.sum = 0
        self.max_size = size
        self.queue = collections.deque()


    def next(self, val):
        self.sum = self.sum + val
        self.queue.append(val)
        
        if len(self.queue) > self.max_size:
            self.sum = self.sum - self.queue.popleft()
        
        return self.sum / len(self.queue)
        
 
 
 
# Median 
"""
m               n
maxheap        minheap     num                   
                              1 
1                             0  
0               1             2      add to maxheap and minheap in turn
0 1             2             3      if -self.maxheap[0] > self.minheap[0]: switch
0 1             2 3           4      
0 1 2           3 4           2
0 1 2           2 3 4


        
"""
class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []
        

    def addNum(self, num: int) -> None:
        m, n = len(self.maxheap), len(self.minheap)
        if m == n:
            heapq.heappush(self.maxheap, -num)
        if m > n:
            heapq.heappush(self.minheap, num)
        
        if len(self.minheap) == 0:
            return
        
        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
   

    def findMedian(self):
        m, n = len(self.maxheap), len(self.minheap)
        if m > n:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        

