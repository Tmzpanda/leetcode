"""
memoization 
# 139. Word Break - if possible - dp O(n^2)
                  - all solutions - dfs memoization
# 236. LCA of a Binary Tree - d&q O(n) O(n)(recursion stack)
# 329. Longest Increasing Subarray - 2d - dfs memoization



backtrack
# 126. Word Ladder - all possible solutions - bfs + dfs backtrack
# 40. Combination Sum - all solutions - backtrack O(2^n)
# 113. Binary Tree Path Sum - all solutions - traverse O(n)
# 79. Word Search - if exists - dfs O(mn * 3^length)



return
# quick select - partition
            
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
                
                   
                  
# 329. Longest Increasing Subarray - 2d - dfs memoization
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        record = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                record[i][j] = self.dfs(matrix, i, j, memo)
                
        return max(map(max, record))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if self.isValid(matrix, x_next, y_next) and matrix[x][y] < matrix[x_next][y_next]:
                longest = max(longest, self.dfs(matrix, x_next, y_next, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
      

# ********************************************* backtrack **********************************************************
# 40. Combination Sum - all solutions - backtrack O(2^n)
class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []
        self.dfs(nums, 0, target, [], result)
        return result
        
    def dfs(self, nums, index, target, subset, result):
        if target < 0:
            return 
        
        if target == 0:
            result.append(list(subset)) 
            return
        
        for i in range(index, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and i != index:    # deduplicate
                continue
            subset.append(nums[i])
            self.dfs(nums, i + 1, target - nums[i], subset, result)   # used once
#             self.dfs(nums, i, target - nums[i], subset, result)     # repeated use
#             self.dfs(nums, target - nums[i], subset, result)        # different sequences are counted as different combinations
            subset.pop()

  
  
# 126. Word Ladder - all possible solutions - bfs + dfs backtrack
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

            
# 79. Word Search - if exists - dfs O(mn * 3^length)
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

      
      
# ********************************************* return **********************************************************    
# recursion top-down with return
def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        return partition(nums, start, r, k)
    if k >= l:
        return partition(nums, l, end, k)
        
    return nums[k]


# recursion top-down
def kthSmallest(nums, k):
    partition(nums, 0, len(nums - 1), k - 1)

    return nums[k - 1]


def partition(nums, start, end, k):

    l, r = start, end
    pivot = nums[(start + end) // 2]

    while l <= r:
        while l <= r and nums[l] < pivot:
            l += 1
        while l <= r and nums[r] > pivot:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    if k <= r:
        partition(nums, start, r, k)
    if k >= l:
        partition(nums, l, end, k)

