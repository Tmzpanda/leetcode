""""
# Word Ladder - length - bfs O(m^2 * n) O(m^2 * n), where m = len(s)
                       - bidirectional bfs O(m^2 * n) O(m^2 * n)
              - all possible solutions - bfs + dfs backtrack
              




# Word Break - world - if possible/number of solutions - dp O(n^2)
                     - all solutions - dfs memoization (recursion top-down with return)  
# Decode Ways - dp - O(n)   


# Word Search - one word - dfs T << O(m*n * 3^len(word))
              - several words - prefix backtrack 
              
# Word Pattern - given string is separated - O(n)
               - given string is not separated - dfs O(len(string)^len(pattern))

# Wildcard - dp O(m*n)





# Word Search - several words - prefix + back track
"""
prefix set - trim 
backtrack - all solutions

x x x x x x 
x     # 
x   # o #              
x     # 
x 

"""
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])
        words = set(words)
        prefix = set()
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])
          
        result = set()
        for i in range(m):
            for j in range(n):
                substring = board[i][j]
                self.search(board, i, j, substring, set([(i, j)]), words, prefix, result)
        
        return list(result)
    
    def search(self, board, x, y, substring, visited, words, prefix, result):
        if substring not in prefix:     # trim 
            return 
        
        if substring in words:
            result.add(substring)
        
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if not self.isValid(board, x_next, y_next, visited):
                continue
    
            visited.add((x_next, y_next))
            self.search(board, x_next, y_next, substring + board[x_next][y_next], visited, words, prefix, result)
            visited.remove((x_next, y_next))
            
            
    def isValid(self, grid, i, j, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        return True



# *********************************************** Word Pattern **************************************************************
# Word Pattern 
 # given string is separated - O(n)
 """
                                  abab  "red blue red blue"
                     a "red"                                 
                     b "blue"           
 
 """
 def wordPattern(pattern, string):
        words = string.split()
        if len(words) != len(pattern):
            return False
        
        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    return False
                
            else:
                if words[i] in mapping.values(): # one to one mapping
                    return False
                mapping[pattern[i]] = words[i]
                
        return True
        


# given string is not separated - O(len(string)^len(pattern))

"""
                                 abab  "redblueredblue"
                  a "r"    ...                            a "red"      ...   a "redbl"             
 b "e"  b "edb" ... b "eblue"  ...
 
 
# of matching for each recursion: len(string)
# of recursion: len(pattern) 
# time complexity = len(string) ^ len(pattern)  

"""
class Solution:
    
    def wordPatternMatch(self, pattern, string):
        return self.is_match(pattern, string, {}, set())
        
        
    def is_match(self, pattern, string, char_to_word, used):
        # break condition
        if not pattern:
            return not string
        
        char = pattern[0]
        
        # if pattern exists
        if char in char_to_word:
            word = char_to_word[char]
            if not string.startswith(word):
                return False        
            return self.is_match(pattern[1:], string[len(word):], char_to_word, used)
        
        # if pattern hasn't been assigned yet
        for i in range(len(string)):
            word = string[:i + 1]
            if word in used:        # one to one mapping
                continue
            
            used.add(word)
            char_to_word[char] = word
            
            if self.is_match(pattern[1:], string[i + 1:], char_to_word, used):
                return True     
                
            del char_to_word[char]
            used.remove(word)
            
        return False

      
#*********************************************** Wildcard **************************************************************
# Wildcard
"""

    "" a b b b 
  "" T F F F F
  a  F # 
  *  ￬   #        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] if pattern[i] == '*'
  b  F
  ?  F     #      dp[i][j] = dp[i - 1][j - 1] if pattern[i - 1] == '?' or pattern[i - 1] == string[j - 1]


"""
# dp O(m*n)
def isMatch(s, p):

    m = len(p)
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(1, m + 1):
        if p[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
            
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[i - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                
    return dp[m][n]



