# 212. Word Search - several words - trie
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
