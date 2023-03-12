# 126. Word Ladder - all possible solutions - bfs + dfs
from collections import deque
class Solution:
    
    def findLadders(self, start, end, dict):
        dictionary = set(dict)
        dictionary.add(start)
        dictionary.add(end)

        # build graph
        word_to_distance = self.bfs(end, dictionary)  
        
        # backtrack
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
            for char in "abcdefghijklmnopqrstuvwxyz":
                next_word = left + char + right
                if next_word != word and next_word in dictionary:
                    words.append(next_word)
    
        return words
        
        
    def dfs(self, word, end, word_to_distance, path, result, dictionary):
        if word == end:
            result.append(path[:])
            return

        for next_word in self.get_next_words(word, dictionary):
            if word_to_distance[next_word] != word_to_distance[word] - 1:   # shortest
                continue
            path.append(next_word)
            self.dfs(next_word, end, word_to_distance, path, result, dictionary)
            path.pop()
