# 127. Word Ladder - shortest path - bfs O(n * m^2), where m = len(s)
from collections import deque
class Solution:
    def ladderLength(self, start, end, dict):
        
        dictionary = set(dict)
        dictionary.add(end)
        
        queue = deque([start])      
        visited = set()             # visited
        level = 0
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

  
# bidirectional bfs - O(n * m^2), where m = len(s)
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