# 140. Word Break - all solutions - dfs memoization O(n^2)
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
                
                