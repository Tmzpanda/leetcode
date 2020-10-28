"""
# subarrays O(n^2)
# Longest Increasing Subarray - 1d increasing/monotonous - greedy O(n)
                               - 2d matrix - dfs memoization
# Longest Palindrome Substring - middle out O(n^2)
                               - dp O(n^2)
      
      
      
# subarraySum - prefix sum
# Maximum Subarray - greedy O(n)
# Subarray Sum Equals K - hashmap O(n)



# Shortest Subarray with Sum at Least K - sliding window O(n)
# Minimum Window Substring - two pointers O(S + T)
# Minimum Window Subsequence - dp O(ST)
                             - two pointers O(ST) = O((# of pattern found)*S*T)



"""

  

#************************************************************ Longest Subarray ********************************************************************
# subarrays O(n^3)
def findSubarrays(nums):
    n = len(nums)
    subarrays =  []
    
    for i in range(n):
        for l in range(i, n):
            subarray = nums[i, l + 1]
        subarrays.append(subarray)
                
    return subarrays
                
nums = [1, 2, 3, 4, 5]
findSubarray(nums)



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

 
 
# Longest Increasing Subarray 2d
# dfs memoization
"""
        0 1 2 3 4..... n
      0     #
      1   # x #
      2     #
      3      
      4
      .
      .
      m

""" 
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestContinuousIncreasingSubsequence2(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        dp = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = self.dfs(matrix, i, j,  memo)
                
        return max(map(max, dp))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_prev, y_prev = x - delta_x, y - delta_y
            if not self.isValid(matrix, x_prev, y_prev) or matrix[x][y] <= matrix[x_prev][y_prev]:
                continue
            longest = max(longest, self.dfs(matrix, x_prev, y_prev, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])
      
      
      

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


#*********************************************************** Subarray Sum *************************************************************************
# Maximum Subarray - greedy O(n) 
def maxSubArray(nums):
    minSum, maxSum = 0, -sys.maxsize
    prefixSum = 0
    
    for num in nums:
        prefixSum += num
        maxSum = max(maxSum, prefixSum - minSum)
        minSum = min(minSum, prefixSum)
        
    return maxSum

  
# Subarray Sum Equals K  O(n) 
from collections import defaultdict
def subarraySum(nums, k):
    
    n = len(nums)
    psum = 0
    psum_to_freq = defaultdict(int)
    psum_to_freq[0] = 1
    res = 0
    
    for i in range(n): 
        psum += nums[i]
        if psum - k in psum_to_freq:
            res += psum_to_freq[psum - k]
            
        psum_to_freq[psum] += 1
    return res

  
# Subarray Sum Equals nK  O(n) 
"""
sum(nums[0 to i]) = aK + b
sum(nums[0 to j]) = cK + d
sum(nums[i+1 to j]) = (c-a)K + (d-b)

"""
def checkSubarraySum(nums, k):
    n = len(nums)
    psum = 0
    psum_mod_k_to_index = {0: -1}     
    res = 0

    for i in range(n): 
        psum += nums[i]
        if k != 0:                             
            psum_mod_k = psum % k
        else:
            psum_mod_k = psum
            
        if psum_mod_k in psum_mod_k_to_index:
            if i - psum_mod_k_to_index[psum_mod_k] >= 2:    # psum_mod_k_to_index[psum_mod_k] + 1 to i
                return True
        else:
            psum_mod_k_to_index[psum_mod_k] = i             # do not replace index of the same psum_mod_k value

    return False
  
  
#*********************************************************** Minimum Window ************************************************************************
# Minimum Window Substring
"""
S = "azjskfzts"      T = "sz"
     -  -      expand
      - -      contract 
       --   
       - -
"""
# two pointers O(S + T)
class Solution:
    def minWindow(self, s, t):
        targetCharToFreq = self.buildCharToFreq(t)
        sourceCharToFreq = {}
        matched, n = 0, len(targetCharToFreq)
        
        window = ""
        minLen = sys.maxsize
        l, r = 0, 0
        while r < len(s):
            sourceCharToFreq[s[r]] = sourceCharToFreq.get(s[r], 0) + 1
            if s[r] in targetCharToFreq and sourceCharToFreq[s[r]] == targetCharToFreq[s[r]]:
                    matched += 1

            while matched == n and l <= r: #
                windowLen = r - l + 1
                if windowLen < minLen:
                    minLen = windowLen
                    window = s[l: r + 1]

                sourceCharToFreq[s[l]] -= 1
                if s[l] in targetCharToFreq and sourceCharToFreq[s[l]] < targetCharToFreq[s[l]]:
                    matched -= 1
                l += 1      
                
            r += 1

        return window

        
    def buildCharToFreq(self, s):
        targetCharToFreq = {}
        for c in s:
            targetCharToFreq[c] = targetCharToFreq.get(c, 0) + 1
        return targetCharToFreq
        
        
# Shortest Subarray with Sum at Least K - sliding window O(n)
"""
A =       [1, 3, -1, 3, 1]    K = 5
psum = [0, 1, 4,  3, 6, 7]

queue [0, 1, 4]
      [0, 1, 3]
      [0, 1, 3, 6]
         [1, 3, 6]   shortest = i - queue.popleft()
            [3, 6, 7]
"""
import sys
from collections import deque

def shortestSubarray(A, K):
    n = len(A)
    psum = [0] * (n + 1)
    
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + A[i - 1] 
    
    queue = deque()
    shortest = sys.maxsize
    for i, s in enumerate(psum):
        while queue and s <= psum[queue[-1]]:
            queue.pop()
        
        while queue and  s - psum[queue[0]] >= K:
            shortest = min(shortest, i - queue.popleft())
            
        queue.append(i)
        
    return shortest if shortest != sys.maxsize else -1
            
            
            
        

  

  






