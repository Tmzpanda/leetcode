"""
# Trie
# 211. Design Trie
# 212. Word Search - several words - Trie


# LinkedList
# 146. LRU Cache
# 685. First Unique Number - Data Stream 
# 707. Design LinkedArrayList


# Array
# 622. Design CircularArray
# 380. RandomizedSet Insert Delete GetRandom O(1) 


# Stack - Queue - Heap
# 402. Remove K Digits Smallest Possible - mono-stack O(n)
# 862. Shortest Subarray with Sum at Least K - negative exists - mono-queue O(n)
# 295. Find Median from Data Stream - heap

"""
# *********************************************** Trie **************************************************************
# 211. Design Trie
class TrieNode: 
    def __init__(self,val):
        self.children = {}             # char_to_node
        self.end = False
        

class WordDictionary:
    def __init__(self):
        self.root = TrieNode(0)        
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.end = True
            
            
    def search(self, word: str) -> bool:
        def dfs(i, node):
            # break
            if i == len(word):
                return node.end
            
            if word[i] != '.':
                if word[i] not in node.children:
                    return False
                return dfs(i + 1, node.children[word[i]])
            
            else:
                for node in node.children.values():
                    if dfs(i + 1, node):
                        return True
                return False
        
        return dfs(0, self.root)
    

# 212. Word Search - several words - Trie
class TrieNode:			
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
             
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word):	
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()  
            node = node.children[c]     		
        node.is_word = True
        node.word = word   
        
              
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        
        # add
        trie = Trie()
        for word in words:		
            trie.add(word)
        
        # search
        result = set()
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                node = trie.root.children.get(char)
                self.dfs(board, i, j, node, set([(i, j)]), result)
        
        return list(result)
    
    
    def dfs(self, board, x, y, node, visited, result):
        if node is None:
            return
        
        if node.is_word: 
            result.add(node.word) 
        
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if not self.isValid(board, x_next, y_next, visited):
                continue
    
            visited.add((x_next, y_next))
            self.dfs(board, x_next, y_next, node.children.get(board[x_next][y_next]), visited, result)   # backtrack
            visited.remove((x_next, y_next))
            
            
    def isValid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
          
        return True
    
# ********************************************** LinkedList ************************************************************
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


        
# ********************************************** Array ************************************************************
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



# 380. RandomizedSet Insert Delete GetRandom O(1) 
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True 

    def remove(self, val: int) -> bool:         # O(1) remove in an array
        if val not in self.val_to_index:
            return False
        
        index = self.val_to_index[val]
        last_value = self.nums[-1]
        
        self.nums[index] = last_value
        self.val_to_index[last_value] = index
        self.nums.pop()
        del self.val_to_index[val]
        
        return True
        
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]    
    
    

# *********************************************** Stack - Queue - Heap **************************************************************
# 402. Remove K Digits Smallest Possible - mono-stack O(n)
def removeKdigits(num, k):
    stack = []
    for char in num:
        while stack and k and int(stack[-1]) > int(char):       # increasing
            stack.pop()
            k -= 1
        stack.append(char)

    while k:          
        stack.pop()
        k -= 1
    if not stack:
        return '0'

    return str(int("".join(stack)))

    
    
# 862. Shortest Subarray with Sum at Least K - negative exists - mono-queue O(n)
import sys
from collections import deque
def shortestSubarray(A, K):
    shortest = sys.maxsize
    psum = 0
    queue = deque([(-1, 0)])        # (end, psum)

    for end in range(len(A)):
        psum += A[end]

        while queue and psum - queue[0][1] >= K:
            shortest = min(shortest, end - queue.popleft()[0])
        
        while queue and queue[-1][1] >= psum:     # increasing
            queue.pop()
            
        queue.append((end, psum))

    return shortest if shortest != sys.maxsize else -1



# 295. Find Median from Data Stream
"""
num             maxheap      minheap
1                -1
0                               0
2               -2, -1          0
                -1, 0           2
  
maxheap keeps track of LOWER bound of median
minheap .............. HIGHER bound ........

"""
class MedianFinder:

    def __init__(self):
        self.minheap, self.maxheap = [], []
        

    def addNum(self, num: int) -> None:
        m, n = len(self.maxheap), len(self.minheap)
        if m == n:
            heappush(self.maxheap, -num)
        if m > n:
            heappush(self.minheap, num)
        
        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))
   

    def findMedian(self):
        m, n = len(self.maxheap), len(self.minheap)
        if m > n:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2

