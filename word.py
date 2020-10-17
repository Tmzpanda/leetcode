""""
# Word Ladder - bfs
              - dp




# Word Break - if possible solution exists - dp O(n^2)
             - number of possible solutions - dp O(n^2)
             - all possible solutions           
# Decode Ways - dfs 
              - dp
# Word Pattern       
# Wildcard Matching






# Levenshtein distance



"""
# Word Ladder - dp






# *********************************************** Word Break **************************************************************

# Word Break - if solution exists - dp O(n^2)
"""
    s     l e e t c o d e
   dp   T       x = dp[i] and s[i to j-1] in wordSet    
        i       j
        
"""
def wordBreak(s, wordSet):
       
    n = len(s)
    dp = [False for _ in range(n + 1)] 
    dp[0] = True
   
    for i in range(n + 1):
       for j in range(i + 1, n + 1):
           dp[j] = dp[i] and s[i: j] in wordSet
              
    return dp[n]


# Word Break - number of solutions - dp O(n^2)
def wordBreak(s, dict):
    n = len(s)
    s = s.lower()
    wordSet = set([word.lower() for word in dict])
    
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1   
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if s[i: j] in wordSet:
                dp[j] += dp[i]     
                
    return dp[n]


# Word Break - all solutions 
"""
                              "catsanddogs"
                  cat "sanddogs"        cats "anddogs"    
                    sand "dogs"               and "dogs"     
                         dogs ""                   dogs ""

"""
class Solution:

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict, {})
        
    def dfs(self, s, wordDict, memo):

        if s in memo:
            return memo[s]
        
        partitions = []
        if s in wordDict:
            partitions.append(s)
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        memo[s] = partitions    
        return partitions



# Decode Ways      
# dp
"""

                                    "2263"
                          2 "263"               22 "63" <-------------- same 
    same  -------> 2 "63"        26 "3"             6 "3"
                      6 "3"          3 ""              3 ""
                         3 ""


dp O(n)
dp[i] = dp[i - 1]*(if "s[i - 1]" is valid) + dp[i - 2]*(if "s[i - 2]s[i - 1]" is valid)

"""
class Solution:
    def numDecodings(self, s):
        if s.startswith('0'):
            return 0
        
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * self.isValid(s[i - 1]) + dp[i - 2] * self.isValid(s[i - 2: i])
            
        return dp[n]
    
    def isValid(self, string):
        n = len(string)
        num = int(string)
        if n == 1 and 1<= num <= 9:
            return 1
        if n == 2 and 10 <= num <= 26:
            return 1
        return 0
        

# Decode Ways - wildcard match











