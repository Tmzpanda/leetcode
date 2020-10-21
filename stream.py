"""
# data structure
# First Unique

# stats
# Moving Average
# Median

"""

#********************************* stats **********************************************
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
        

