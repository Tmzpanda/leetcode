"""
# 139. Word Break 
# 132. Palindrome Partitioning - minimum cut  
# 583. Delete Distance 
# 416. Partition Equal Subset Sum



"""


# 139. Word Break - dp O(n^2)
def wordBreak(s, wordDict):
    
    def dfs(s, wordDict, memo):
        if s in memo:
            return memo[s]
        
        if not s:
            return 1
    
        res = 0
        for i in range(len(s)):
            if s[: i + 1] in wordDict:
                res += dfs(s[i + 1:], wordDict, memo)
                
        memo[s] = res
        return res
    
    return dfs(s, wordDict, {})
      
      
# 132. Palindrome Partitioning - minimum cut - dp O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            
            if isPalindrome(s):
                return 0
            
            res = len(s) - 1
            for i in range(len(s)):
                if isPalindrome(s[: i + 1]):
                    res = min(res, 1 + dfs(s[i + 1:], memo))
                    
            memo[s] = res
            return res
        
        return dfs(s, {})
            

# 583. Delete Distance - dp O(m*n)
def minDistance(word1: str, word2: str) -> int:

    def dfs(word1, word2, memo):
        if (word1, word2) in memo:
            return memo[(word1, word2)]

        if word1 == word2:
            return 0

        if word1 == "":
            return len(word2)

        if word2 == "":
            return len(word1)

        if word1[0] == word2[0]:
            res = dfs(word1[1:], word2[1:], memo)

        else:
            res = min(dfs(word1, word2[1:], memo) + 1,
                      dfs(word1[1:], word2, memo) + 1
                     )

        memo[(word1, word2)] = res
        return res

    return dfs(word1, word2, {})


# 416. Partition Equal Subset Sum - dp O(n*S)
def canPartition(nums):
    
    if sum(nums) % 2 != 0 or max(nums) > sum(nums)//2:
            return False

    n = len(nums)
    S = sum(nums) // 2

    def dfs(nums, target, memo):
        if target in memo: 
            return memo[target]

        if target < 0: 
            return False
        if target == 0: 
            return True

        res = False
        for i in range(len(nums)):
            if dfs(nums[i+1:], target-nums[i], memo): 
                res = True

        memo[target] = res
        return res

    return dfs(nums, S, {})


# 1043. Partition Array for Maximum Sum
# 410. Split Array Largest Sum
# 698. Partition to K Equal Sum Subsets
