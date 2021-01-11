"""
# dummy node
# merge


# pointers
# hasCycle
# middleNode
# Remove Nth Node from the end - one pass
# reverse 
          


# data structure
# LRU
# First Unique Number in Data Stream


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
    
 

#********************************* pointers **********************************************
# hasCycle
# 2 pointers
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


# middle node
"""
 1 -> 2 -> 3 -> 4
           f
      s
"""
def middleNode(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


# Remove Nth Node from the end - one pass
"""
 dummy -> 1 -> 2 -> 3 -> 4              n = 2
                         f          
               s
"""

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    
    for _ in range(n):
        fast = fast.next   
        
    while fast.next:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    
    return dummy.next



# reverse
# 3 pointers
"""
prev cur next
      1 -> 2 -> 3 -> None
     
"""
def reverse(head):
    prev = None
    while head:
        nxt = head.next

        head.next = prev
        prev = head
        head = nxt

    return prev



    




#********************************* data structure **********************************************
# LRU
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



# First Unique Number in Data Stream 
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
        
            














