"""
# Trie
# 211. Design Trie
# 212. Word Search - several words - Trie


# Stream
# 146. LRU Cache
# 685. First Unique Number - Data Stream 
# 707. Design LinkedArrayList


# Heap
# 295. Find Median from Data Stream

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
    
# ********************************************** Stream ************************************************************
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
            
    def get(self, index):
        return self.idx_to_prev[self.head.idx + index].next.val
    
    def put(self, index, value):
        self.idx_to_prev[self.head.idx + index].next.val = value

        
# ********************************************** LinkedList ************************************************************
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
            heappush(self.maxheap, -num)
        if m > n:
            heappush(self.minheap, num)
        
        if len(self.minheap) == 0:
            return
        
        if -self.maxheap[0] > self.minheap[0]:
            heappush(self.maxheap, -heappop(self.minheap))
            heappush(self.minheap, -heappop(self.maxheap))
   

    def findMedian(self):
        m, n = len(self.maxheap), len(self.minheap)
        if m > n:
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) / 2

 
        
