"""
memoization 
# 139. Word Break - if possible - dp O(n^2)
                  - all solutions - dfs memoization



backtrack
# 126. Word Ladder - all possible solutions - bfs + dfs

"""

# ********************************************* memoization **********************************************************
# 139. Word Break - if possible - dp O(n^2)
class Solution:

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return True
        
        res = False
        for i in range(0, len(s)):
            prefix = s[:i + 1]
            if prefix not in wordDict:
                continue

            if self.dfs(s[i + 1:], wordDict, memo):
                res = True
                
        memo[s] = res      
        return res


# 139. Word Break - all solutions - dfs memoization O(n^2)
#                                 - backtrack O(2^n) TLE
class Solution:
    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        partitions = []
        if s in wordDict:
            partitions.append(s)
        
        # recursion
        for i in range(len(s)): 
            prefix = s[:i + 1]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i + 1:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        memo[s] = partitions    
        return partitions
 

# backtrack TLE
class Solution:
    def wordBreak(self, s, wordDict):
        result = []
        self.dfs(s, [], result, wordDict)
        return result
        
    def dfs(self, s, combination, result, wordDict):

        if not s:
            result.append(" ".join(combination))
        
        for i in range(0, len(s)): 
            prefix = s[:i + 1]
            
            if prefix in wordDict:              # backtrack
                combination.append(prefix)
                self.dfs(s[i + 1:], combination, result, wordDict)
                combination.pop()
                
                
                

# ********************************************* backtrack **********************************************************
# 126. Word Ladder - all possible solutions - bfs + dfs
from collections import deque
class Solution:
    
    def findLadders(self, start, end, dict):
        dictionary = set(dict)
        dictionary.add(start)
        dictionary.add(end)

        word_to_distance = self.bfs(end, dictionary)    # build graph
        result = []
        self.dfs(start, end, word_to_distance, [start], result, dictionary)     # backtrack
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
            if word_to_distance[next_word] != word_to_distance[word] - 1:  # shortest
                continue
            path.append(next_word)
            self.dfs(next_word, end, word_to_distance, path, result, dictionary)
            path.pop()

        

