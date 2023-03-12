# 91. Decode Ways - number of solutions - dp O(n)
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


# 91. Decode Ways - number of solutions - dp O(n)
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