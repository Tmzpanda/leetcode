"""
# Longest Increasing Substring - greedy O(n)
# Longest Palindrome Substring - middle out O(n^2)
                               - dp O(n^2)
                               
     
# subarraySum -      
# prefix sum
# Minimum Window Subsequence - pointers O(ST) O((# of pattern found)*S*T)




"""

#********************************* Longest Subarray **********************************************
# Longest Increasing Subarray - greedy O(n)
def LIS(nums):
    if not nums:
        return 0
    
    longest = 1
    flag = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]: 
            flag = i
        longest = max(longest, i - flag + 1)
        
    return longest

  
# Longest Monotonous Subarray 
def LIS(nums):
    if not nums:
        return 0
    
    longest = 1
    increasingFlag, decreasingFlag = 0, 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]: 
            increasingFlag = i

        elif nums[i] > nums[i - 1]:
            decreasingFlag = i
               
        elif nums[i] == nums[i - 1]:
            increasingFlag = i
            decreasingFlag = i
        
        longest = max(longest, i - increasingFlag + 1, i - decreasingFlag + 1)

    return longest


  
# Longest Palindrome Substring - middle out O(n^2)
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


#********************************* Subarray Sum **********************************************







#********************************* **********************************************
# Minimum Window Subsequence 
# pointers - O((# of pattern found)*S*T) = O(ST)
def minWindow(S, T):
        
    minLen = len(S) + 1
    window = ""

    i, j = 0, 0
    while i < len(S):
        if S[i] == T[j]:
            j += 1
        if j == len(T):
            end = i 
            j -= 1
            while j >= 0:
                if S[i] == T[j]:
                    j -= 1
                i -= 1
            i += 1
            j += 1
            if end - i + 1< minLen:
                minLen = end - i + 1
                window = S[i:end + 1]
        i += 1
    return window
  
# 



# find all subarrays O(n^3)
def findSubarrays(nums):
    n = len(nums)
    subarrays =  []
    
    for i in range(n):
        for l in range(i, n):
            
            subarray = []
            for j in range(i, l + 1):
                subarray.append(nums[j])
            subarrays.append(subarray)
                
    return subarrays
                
nums = [1, 2, 3, 4, 5]
findSubarray(nums)





