# 5. Longest Palindromic - Substring 
# 2 pointers O(n^2)
class Solution:
    def LPS(self, s):
        if not s:
            return ""
        
        longest = ""
        for middle in range(len(s)):
            sub1 = self.findPalindrome(s, middle, middle)
            sub2 = self.findPalindrome(s, middle, middle + 1)
            sub = max(sub1, sub2, key=lambda x: len(x))
            if len(sub) > len(longest):
                longest = sub
                
        return longest
        
    def findPalindrome(self, string, l, r):
        while l >= 0 and r < len(string):
            if string[l] != string[r]:
                break
            l -= 1
            r += 1
        
        l, r = l + 1, r - 1
        return string[l:r + 1]



# dp O(n^2)
"""
  a d b b c a
a T         x = s[i] == s[j] && dp[i + 1][j - 1]
d T T     
b   T T
b     T T
c       T T
a         T T
"""
def LPS(s):
      if not s:
          return ""

      n = len(s)
      dp = [[False] * n for _ in range(n)]

      for i in range(n):
          dp[i][i] = True
      for i in range(1, n):
          dp[i][i - 1] = True

      start, end = 0, 0
      longest = 1
      for length in range(1, n):        
          for i in range(n - length):
              j = i + length
              dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
              if dp[i][j]:
                  longest = length + 1
                  start, end = i, j

      return s[start:end + 1]