"""
# top-down
# dfs memoization
# d&q


# bottom-up
# backtrack



# comparison
# Word Break - dfs memoization
# Word Ladder - backtrack


                                    "2263"
                          2 "263"               22 "63" <-------------- same 
    same  -------> 2 "63"        26 "3"             6 "3"
                      6 "3"          3 ""              3 ""
                         3 ""


        26*len(s)
        x 
        x
hit -> hot -> dot -> dog -> cog
        o  ->  o ->   o  -> cog
        .      
        .      
        o  ->  o ->   o  ->  o -> o -> cog  
        x






"""
#********************************* top-down ****************************************
# Decode Ways
"""         
dfs memoization

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
        if not s or s[0] == '0':
            return 0

        return self.dfs(s, {})


    def dfs(self, s, memo):
        if s in memo:
            return memo[s]

        if not s:
            return 1

        res = 0
        for i in (1, 2):
            if len(s[:i]) == i and self.isValid(s[:i]):
                res += self.dfs(s[i:], memo)

        memo[s] = res
        return res

    
    def isValid(self, s):
        n = len(s)
        num = int(s)
        if n == 1 and 1 <= num <= 9:
            return True
        if n == 2 and 10 <= num <= 26:
            return True

        return False







