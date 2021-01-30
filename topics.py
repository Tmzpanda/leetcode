"""
121. Sell Stock - Subsequence Maximum Diffs - one transaction - greedy O(n)
122.                                        - ∞ transactions - greedy O(n) 
188.                                        - at most K transactions - dp O(n*k)
309.                                        - ∞ transactions with cooldown - dp O(n)
714.                                        - ∞ transactions with transaction fee - dp O(n)


198. Rob House - Non-adjacent Elements Sum - array - dp O(n)
213.                                       - cycle - dp O(n)
337.                                       - tree - d&q O(n)


139. Word Break - if possible - dp O(n^2)
                - all solutions - dfs memoization                
127. Word Ladder - shortest path - bfs O(n * m^2)
                                 - bidirectional bfs
126.             - all possible solutions - bfs + dfs

79. Word Search - if exists - dfs O(mn * 3^length)
211.            - data structure - trie

290. Word Pattern - given string is separated - O(n)
                  - given string is not separated - dfs O(len(string)^len(pattern))
44. Wildcard Matching - dp O(m*n)



"""
# ********************************************** Stock *******************************************************
# 121. Sell Stock - one transaction - greedy O(n)
import sys
def maxProfit(prices):
    minPrice = sys.maxsize
    maxProfit = 0
    
    for price in prices:
        maxProfit = max(price - minPrice, maxProfit)
        minPrice = min(price, minPrice)
            
    return maxProfit
  
  
# 122. Sell Stock - ∞ transactions - greedy O(n) 
def maxProfit(prices):
    n = len(prices)
    profit = 0
    
    for i in range(1, n):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i - 1]
            
    return profit
  
  
# 188. Sell Stock - at most K transactions -> O(k*n)
  
"""
prices = [3,2,6,5,0,3] k = 2

  3 2 6 5 0 3
0 0 0 0 0 0 0 
1 0 x = max(dp[i][j - 1],
2 0         max(prices[j] - prices[x] + dp[i - 1][x - 1]), where 0 <= x < j


"""
def maxProfit(k, prices):
    if len(prices) <= 1:
        return 0
    
    n = len(prices)
    dp = [[0] * n for _ in range(k + 1)]
    
    for i in range(1, k + 1):
        profit = -sys.maxsize
        
        for j in range(1, n):
            profit = max(profit, -prices[j - 1] + dp[i - 1][j - 1]) # greedy
            dp[i][j] = max(dp[i][j - 1], prices[j] + profit)

    return dp[-1][-1]
 
    
# 309. Sell Stock - ∞ transactions with cooldown - dp O(n)
"""
     3 2 6 5 0 3
 0 0 0 x = max(dp[i - 1],
               prices[i] - prices[x] + dp[x - 2], where 0 <= x < i
              )
     
"""
import sys
def maxProfit(prices):
    n = len(prices)
    dp = [0] * (n + 2)

    profit = -sys.maxsize
    for i in range(3, n + 2):
        profit = max(profit, -prices[i - 2 - 1] + dp[i - 1 - 2])
        dp[i] = max(dp[i - 1], prices[i - 2] + profit)

    return dp[-1]


# 714. Sell Stock - ∞ transactions with transaction fee - dp O(n)
"""
  1, 3, 2, 8, 4, 9
0 0  x = max(dp[i - 1],
             prices[i] - prices[x] - 2 + dp[x - 1], where 0 <= x < i
             )
  
"""
def maxProfit(prices, fee):
        
    n = len(prices)
    dp = [0] * (n + 1)

    profit = -sys.maxsize
    for i in range(2, n + 1):
        profit = max(profit, -prices[i - 1 - 1] - fee + dp[i - 1 - 1])
        dp[i] = max(dp[i - 1], prices[i - 1] + profit)

    return dp[-1]




# ************************************************* Rob ***********************************************************
# 198. House Robber - array        
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)

        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]

    
# 213. House Robber - cycle
class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        dp1[1], dp1[2] = nums[0], max(nums[0], nums[1])    
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])     

        for i in range(3, n):
            dp1[i] = max(nums[i - 1] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[n - 1], dp2[n - 1])

      
# 337. tree
class Solution:
    def rob(self, root):
        rob, not_rob = self.visit(root)
        return max(rob, not_rob)
        
    def visit(self, root):
        if root is None:
            return 0, 0
        
        left_rob, left_not_rob = self.visit(root.left)
        right_rob, right_not_rob = self.visit(root.right)
        
        rob = root.val + left_not_rob + right_not_rob
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        return rob, not_rob
      
        

# ********************************************** Word *******************************************************
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
            
            visited.add((x_next, y_next))
            if self.dfs(board, x_next, y_next, visited, word, index + 1):
                return True
            visited.discard((x_next, y_next))
        
        return False
            
            
    def isValid(self, grid, i, j, visited, word, index):
        n, m = len(grid), len(grid[0])
        if not (0 <= i < n and 0 <= j < m):
            return False
        if (i, j) in visited:
            return False
        
        return grid[i][j] == word[index]
      
      
      
# 211. Word Search
# trie
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



# 290. Word Pattern - given string is separated - O(n)
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
        
        
# 291. Word Pattern - given string is not separated - dfs O(len(string)^len(pattern))
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

    
# 44. Wildcard Matching - dp O(m*n)
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




