# Trie
# 211. Word Search Data Structure - trie
# 212.



# Heap



# Stream
# 146. LRU Cache
# 685. First Unique Number - Data Stream 
# 346. Moving Average 
# 295. Find Median from Data Stream



# 707. Design LinkedArrayList
# CircularArray




# *********************************************** Trie **************************************************************
# 79. Word Search - if exists
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, {(i, j)}, word, 1):
                        return True
        return False
    
    
    def dfs(self, board, x, y, visited, word, index):
        if index == len(word):
            return True
        
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if not self.isValid(board, x_next, y_next, visited, word, index):
                continue
            
            visited.add((x_next, y_next))        # backtrack
            if self.dfs(board, x_next, y_next, visited, word, index + 1):
                return True
            visited.remove((x_next, y_next))
        
        return False
            
            
    def isValid(self, grid, i, j, visited, word, index):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        return grid[i][j] == word[index]
    
    
    
# *********************************************** Heap ************************************************************





# ********************************************** Stream ************************************************************
# 146. LRU Cache
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
    

    
# 346. Moving Average - Data Stream
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
        

        
# 295. Find Median from Data Stream
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




# ********************************************** LinkedList ************************************************************
# LinkedArrayList
class Node:  # DoubleLinkedList 
    def __init__(self, idx, val):
        self.idx = index
        self.val = value
        self.prev = None  
        self.next = None
        

class LinkedArrayList:
    def __init__(self):
        self.size = 0
        self.index_to_node = {}    # O(1) search
        self.head = self.tail = None 
        
        
    def appendFirst(self, val):
        if self.size == 0:
            head = tail = Node(0, val)
            self.index_to_node[0] = head 
        else
            head.prev = Node(head.idx - 1, val)
            head.prev.next = head
            head = head.prev
            self.index_to_node[head.idx] = head
        
        self.size += 1    
        
    def appendLast(self, val):
        if self.size == 0:
            head = tail = Node(0, val)
            self.index_to_node[0] = head 
        else:
            tail.next = Node(tail.idx + 1, val)
            tail.next.prev = tail
            tail = tail.next
            self.index_to_node[tail.idx] = tail
            
        self.size += 1 
        
    def removeFirst():
        del self.index_to_node[head.idx]
        res = head.val
        head = head.next
        size -= 1
        return res
    
    def removeLast():
        del self.index_to_node[tail.idx]
        res = tail.val;
        tail = tail.prev;
        size -= 1
        return res
    
    def get(index):
        return self.index_to_node[head.idx + index].val
    
    def set(index,value):
        self.index_to_node[head.idx + index].val = value



# CircularArray
# public class CircularArray {
#     private int[] A;
#     private int size, head, tail;
    
#     public CircularArray() {
#         A = new int[10];
#     }
    
#     public void appendFirst(int val) {
#         if (size == 0) {
#             A[head] = val;
#             size = 1;
#             return;
#         }
        
#         if (size == A.length) {
#             extend();
#         }
        
#         head = getIndexInArray(head - 1);
#         A[head] = val;
#         size++;
#     }
    
#     public void appendLast(int val) {
#         if (size == 0) {
#             A[head] = val;
#             size = 1;
#             return;
#         }
        
#         if (size == A.length) {
#             extend();
#         }
        
#         tail = getIndexInArray(tail + 1);
#         A[tail] = val;
#         size++;
#     }
    
#     public int removeFirst() {
#         int res = A[head];
#         if (size != 1) {
#             head = getIndexInArray(head + 1);
#         }
        
#         size--;
#         return res;
#     }
    
#     public int removeLast() {
#         int res = A[tail];
#         if (size != 1) {
#             tail = getIndexInArray(tail - 1);
#         }
        
#         size--;
#         return res;
#     }
    
#     public int get(int index) {
#         return A[getIndexInArray(head + index)];
#     }
    
#     public void set(int index, int value) {
#         A[getIndexInArray(head + index)] = value;
#     }
    
#     private int getIndexInArray(int idx) {
#         return (idx + A.length) % A.length;
#     }
    
#     private void extend() {
#         int[] B = new int[A.length * 2];
#         for (int i = 0; i < size; i++) {
#             B[i] = A[(head + i) % A.length];
#         }
        
#         A = B;
#         head = 0;
#         tail = size - 1;
#     }
# }      
        
