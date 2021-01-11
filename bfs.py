"""

# shortest path
# Word Ladder - length - bfs O(m^2 * n) O(m^2 * n), where m = len(s)
                       - bidirectional bfs O(m^2 * n) O(m^2 * n)
              - all possible solutions - bfs + dfs backtrack
# Number Of Islands - bfs
# Knight Shortest Path - bfs
# All nodes Distance K in a Binary Tree - bfs O(n)


# topological sort 
# Course Schedule - if possible solution exists/one possible solution - bfs
# Sequence Reconstruction - bfs



# difference 

1    2    3
x -> x -> x   visited = set()
     ^
  -> x -> x
     2    3
     
     
1    3    4
x -> x -> x  indegree[t]
     ^
  -> x -> x
     2    3
     
"""



#********************************************* Shortest Path **********************************************************
# Word Ladder - shortest path - bfs O(m^2 * n), where m = len(s)
"""
        26*len(s)
        x 
        x
hit -> hot -> dot -> dog -> cog
        o  ->  o ->   o  -> cog
        .      
        .      
        o  ->  o ->   o  ->  o -> o -> cog  
        x
       
"""
from collections import deque

class Solution:
    def ladderLength(self, start, end, dict):
        
        dictionary = set(dict)
        dictionary.add(end)
        
        queue = deque([start])
        level = 0
        visited = set()
        while queue:
            level += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return level
                    
                for next_word in self.get_next_words(word, dictionary): 
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
                        
        return -1
        
    def get_next_words(self, word, dictionary):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word != word and next_word in dictionary:
                    words.append(next_word)
                    
        return words

   
      
# Word Ladder - all possible solutions - bfs + dfs backtrack
from collections import deque
class Solution:
    
    def findLadders(self, start, end, dict):
        dictionary = set(dict)
        dictionary.add(start)
        dictionary.add(end)

        word_to_distance = self.bfs(end, dictionary)
        result = []
        self.dfs(start, end, word_to_distance, [start], result, dictionary)
        return result

    
    def bfs(self, start, dictionary):
        queue = deque([start])
        word_to_distance = {start: 0}

        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dictionary):
                if next_word not in word_to_distance:
                        queue.append(next_word)
                        word_to_distance[next_word] = word_to_distance.get(word, 0) + 1

        return word_to_distance
        

    def get_next_words(self, word, dictionary):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word != word and next_word in dictionary:
                    words.append(next_word)
    
        return words
        
        
    def dfs(self, word, end, word_to_distance, path, result, dictionary):
        
        if word == end:
            result.append(path[:])
            return

        for next_word in self.get_next_words(word, dictionary):
            if word_to_distance[next_word] != word_to_distance[word] - 1:  # shortest
                continue
            path.append(next_word)
            self.dfs(next_word, end, word_to_distance, path, result, dictionary)
            path.pop()

            

# bidirectional bfs - O(m^2 * n), where m = len(s)
class Solution:
    def ladderLength(self, start, end, dict):
        
        dictionary = set(dict)
        dictionary.add(start)
        dictionary.add(end)
        
        word_to_next = {}
        for word in dictionary:
            word_to_next[word] = self.get_next_words(word, dictionary)
            
            
        queue1, queue2 = deque([start]), deque([end])
        visited1, visited2 = {start}, {end}
        
        level = 1           
        while queue1 and queue2:
            level += 1
            self.bfs(queue1, visited1, word_to_next)
            if self.isFound(queue1, visited2):
                return level
              
            level += 1
            self.bfs(queue2, visited2, word_to_next)
            if self.isFound(queue1, visited2):
                return level         
                  
        return 0
    
    
    def isFound(self, queue, visited):
        for word in queue:        
            if word in visited:
                return True
        return False
                  

    def bfs(self, queue, visited, word_to_next):
        for _ in range(len(queue)):
            word = queue.popleft()
            for next_word in word_to_next[word]: 
                if next_word not in visited:
                    queue.append(next_word)
                    visited.add(next_word)
                        
        return -1
    
    
    def get_next_words(self, word, dictionary):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word != word and next_word in dictionary:
                    words.append(next_word)
                    
        return words
        

# BFS
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

class Solution:

    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isValid(grid, i, j, visited):
                    self.bfs(grid, i, j, visited)
                    res += 1
                    
        return res                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in DIRECTIONS:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.isValid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
    
    def isValid(self, grid, i, j, visited):
            
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        
        return int(grid[i][j])


  
        
# All nodes Distance K in a Binary Tree - bfs O(n)
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        nodeToParent = {}
        self.findParent(root, None, nodeToParent)
        
        queue = deque([target])
        seen = {target}
        level = 0
        while queue:
            if level == K:
                return [node.val for node in queue]
           
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nextNode in (node.left, node.right, nodeToParent[node]):  # bidirectional
                    if nextNode and nextNode not in seen:
                        seen.add(nextNode)
                        queue.append(nextNode)    
            
        return []
    
        
    def findParent(self, root, parent, nodeToParent):       # traverse
        node = root
        if node:
            nodeToParent[node] = parent
            self.findParent(node.left, node, nodeToParent)
            self.findParent(node.right, node, nodeToParent)
            
            
            
#********************************************* Topological Sort **********************************************************
# Course Schedule - if possible solution exists/one possible solution - bfs
from collections import deque

def findOrder(numCourses, prerequisites):
  
    out_edges = [[] for _ in range(numCourses)]
    in_degrees = [0 for _ in range(numCourses)]
    for t, f in prerequisites:
        out_edges[f].append(t)
        in_degrees[t] += 1

    queue = deque([node for node in range(numCourses) if in_degrees[node] == 0])
    order = []
    while queue:
        node = queue.popleft()      # not necessarily queue.popoleft() in tops
        order.append(node)
        for next_node in out_edges[node]:
            in_degrees[next_node] -= 1
            if in_degrees[next_node] == 0:
                queue.append(next_node)

    if len(order) == numCourses:
        return order
    return []


# Sequence Reconstruction 
"""
              seq = [5, 2, 6, 3]
          seq[1:] = [2, 6, 3]
zip(seq, seq[1:]) = [(5, 2), ..., (f, t), (6, 3)]


"""
from functools import reduce
def sequenceReconstruction(org, seqs):
    
    nodes = reduce(set.union, seqs, set())   # edge case 
    if nodes != set(org):
        return False

    n = len(org)
    out_edges = [[] for _ in range(n + 1)]
    in_degrees = [0 for _ in range(n + 1)]
    for seq in seqs:
        for f, t in zip(seq, seq[1:]):      # seqs to prerequisites
            out_edges[f].append(t)
            in_degrees[t] += 1

    queue = [node for node in org if in_degrees[node] == 0]
    order = []
    while queue:
        if len(queue) != 1:     # only one sequence
            return False
        node = queue.pop()
        order.append(node)
        for next_node in out_edges[node]:
            in_degrees[next_node] -= 1
            if not in_degrees[next_node]:
                queue.append(next_node)

    return org == order         # reconstruct


