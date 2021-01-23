"""
# Subarray 
53. Maximum Subarray - greedy O(n)
560. Subarray with Sum Equals - K - hashmap O(n)
974. Subarray with Sum Equals - nK - hashmap O(n)

209. Shortest Subarray with Sum at Least K - positive - sliding window O(n)
862. Shortest Subarray with Sum at Least K - negative exists - mono-queue O(n)

3. Longest Substring Without Repeating Characters - sliding window O(n)     
1438. Longest Subarray With Absolute Diff at most K - sliding window O(n)

76. Minimum Window with - Target Characters - sliding window O(n)
727.                    - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)




# Subsequence
674. Longest Increasing Subarray - 1d - greedy O(n)
329.                             - 2d - dfs 
300. Longest Increasing Subsequence - dp O(n^2)
                                    - binary search O(nlogn)  
                                    
1216. K-Palindrome Substring - LPS - dp O(n^2)
131. Palindrome Partioning - all solutions - backtrack
                                           - memoization
132. Palindrome Partioning - minimum cuts - dp O(n^2)

                                    
718. Longest Common - Substring - dp O(m*n)
1143.               - Subsequence - dp O(n^2)   
5. Longest Palindromic - Substring - 2 pointers O(n^2)                  
516.                   - Subsequence - dp O(n^2)

121. Sell Stock - Subsequence Maximum Diffs - one transaction - greedy O(n)
122.                                        - ∞ transactions - greedy O(n) 
188.                                        - at most K transactions - dp O(n*k)
309.                                        - ∞ transactions with cooldown - dp O(n)
714.                                        - ∞ transactions with transaction fee - dp O(n)

198. Rob House - Non-adjacent Elements Sum - array - dp O(n)
213.                                       - cycle - dp O(n)
337.                                       - tree - d&q O(n)


"""
# ************************************************ Subarray *****************************************************************
# 53. Maximum Subarray - greedy O(n)
def maxSubArray(nums):
    minSum, maxSum = 0, -sys.maxsize
    prefixSum = 0
    
    for num in nums:
        prefixSum += num
        maxSum = max(maxSum, prefixSum - minSum)
        minSum = min(minSum, prefixSum)
        
    return maxSum


# 560. Subarray with Sum Equals - K - hashmap O(n)
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


# 974. Subarray with Sum Equals - nK - hashmap O(n)
def subarraysDivByK(nums, k):
    n = len(nums)
    psum = 0
    psumModK_to_freq = {0: 1}     
    res = 0

    for i in range(n): 
        psum += nums[i]
        psumModK = psum % k
        if psumModK in psumModK_to_freq:
            res += psumModK_to_freq[psumModK]
          
        psumModK_to_freq[psumModK] = psumModK_to_freq.get(psumModK, 0) + 1           

    return res


# 209. Shortest Subarray with Sum at Least K - positive - sliding window O(n)
import sys
def shortestSubarray(A, K):
    window_sum = 0
    start = 0
    shortest = sys.maxsize
    
    for end in range(len(A)):
        window_sum += A[end]
        while window_sum >= K:
            shortest = min(shortest, end - start + 1)
            window_sum -= A[start]
            start += 1
            
    return shortest if shortest != sys.maxsize else -1
  
     
# 862. Shortest Subarray with Sum at Least K - negative exists - mono-queue O(n)
import sys
from collections import deque
def shortestSubarray(A, K):
    shortest = sys.maxsize
    psum = 0
    queue = deque([(-1, 0)])     # (end, psum)

    for end in range(len(A)):
        psum += A[end]

        while queue and psum - queue[0][1] >= K:
            shortest = min(shortest, end - queue.popleft()[0])
        
        while queue and psum <= queue[-1][1]:     # increasing
            queue.pop()
            
        queue.append((end, psum))

    return shortest if shortest != sys.maxsize else -1
        
        
# Longest Subarray with Sum at Most K - All Positive
def longestSubarray(A, K):
    window_sum = 0
    start = 0
    longest = -sys.maxsize
    
    for end in range(len(A)):
        window_sum += A[end]
        while window_sum > K:
            window_sum -= A[start]
            start += 1
            
        longest = max(longest, end - start + 1)
      
    return longest if longest != -sys.maxsize else -1   


# 3. Longest Substring Without Repeating Characters - sliding window O(n)     
def lengthOfLongestSubstring(s):
    start = 0
    unique_chars = set()
    longest = 0

    for end in range(len(s)):

        while s[end] in unique_chars:
            unique_chars.remove(s[start])
            start += 1
            
        unique_chars.add(s[end])
        longest = max(longest, end - start + 1)
        
    return longest


# 1438. Longest Subarray With Absolute Diff at most K - sliding window O(n)
from collections import deque
import sys 

class Solution:
    def longestSubarray(self, nums, limit):
        maxq, minq = deque(), deque()
        start = 0
        longest = -sys.maxsize 

        for end in range(len(nums)):
          
            while maxq and nums[end] > maxq[-1]:
                maxq.pop()
            maxq.append(nums[end])

            while minq and nums[end] < minq[-1]:
                minq.pop()
            minq.append(nums[end])

            while maxq[0] - minq[0] > limit:
                if maxq[0] == nums[start]:
                    maxq.popleft()
                if minq[0] == nums[start]:
                    minq.popleft()
                start += 1

            longest = max(longest, end - start + 1)

        return longest


# 76. Minimum Window with - Target Characters - sliding window O(n)
class Solution:
    def minWindow(self, s, t):
        targetCharToFreq = self.buildCharToFreq(t)
        sourceCharToFreq = {}
        n = len(targetCharToFreq)
        matched = 0
        
        window = ""
        minLen = sys.maxsize
        l = 0
        for r in range(len(s)):
            sourceCharToFreq[s[r]] = sourceCharToFreq.get(s[r], 0) + 1
            if s[r] in targetCharToFreq and sourceCharToFreq[s[r]] == targetCharToFreq[s[r]]:
                    matched += 1

            while matched == n: 
                windowLen = r - l + 1
                if windowLen < minLen:
                    minLen = windowLen
                    window = s[l: r + 1]

                sourceCharToFreq[s[l]] -= 1
                if s[l] in targetCharToFreq and sourceCharToFreq[s[l]] < targetCharToFreq[s[l]]:
                    matched -= 1
  
                l += 1  
               
        return window
        
    def buildCharToFreq(self, s):
        targetCharToFreq = {}
        for c in s:
            targetCharToFreq[c] = targetCharToFreq.get(c, 0) + 1
               
        return targetCharToFreq


# 727. Minimum Window with - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)
def minWindow(S, T):
        
    minLen = len(S) + 1
    window = ""

    i, j = 0, 0
    while i < len(S):
        if S[i] == T[j]:
            j += 1
               
        if j == len(T):   # shrink
            end = i 
            j -= 1
            while j >= 0:
                if S[i] == T[j]:
                    j -= 1
                i -= 1
            i += 1
            j += 1
            if end - i + 1 < minLen:
                minLen = end - i + 1
                window = S[i:end + 1]
               
        i += 1
     
    return window
  

# ************************************************* Subsequence ***********************************************************
# 674. Longest Increasing Subarray - 1d - greedy O(n)
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


# 329. Longest Increasing Subarray - 2d - dfs memoization
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        record = [[1 for _ in range(m)] for _ in range(n)]
        memo = {}
        longest = 0
        for i in range(n):
            for j in range(m):
                record[i][j] = self.dfs(matrix, i, j, memo)
                
        return max(map(max, record))
        
    
    def dfs(self, matrix, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        longest = 1
        for delta_x, delta_y in DIRECTIONS:
            x_next, y_next = x + delta_x, y + delta_y
            if self.isValid(matrix, x_next, y_next) and matrix[x][y] < matrix[x_next][y_next]:
                longest = max(longest, self.dfs(matrix, x_next, y_next, memo) + 1)
            
        memo[(x, y)] = longest
        return longest
        
        
    def isValid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

     
# 300. Longest Increasing Subsequence
# dp O(n^2)
def LIS(nums):
    if not nums:
        return 0
    
    n = len(nums)        
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)   


# binary search O(nlogn)
class Solution:
    def lengthOfLIS(self, nums):
            
        temp = [sys.maxsize] * (len(nums) + 1)
        temp[0] = -sys.maxsize
        
        longest = 0
        for num in nums:
            index = self.searchInsert(temp, num)
            temp[index] = num
            longest = max(longest, index)
            
        return longest
            
        
    def searchInsert(self, nums, target):      
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid
            else:
                l = mid
                
        return r


# 718. Longest Common - Substring - O(m * n * min(m,n)) TLE
def longestCommonSubstring(A, B):
        
    longest = 0
    for i in range(len(A)):
        for j in range(len(B)):
            
            l = 0
            while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
                longest = max(longest, l + 1)
                l += 1
            
    return longest


# dp O(n^2)
def longestCommonSubstring(A, B):
        
        if not A or not B:
            return 0
        
        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for i in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n +  1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
        return max(map(max, dp))


# 1143. Longest Common - Subsequence - dp O(n^2)   
"""
  "" A G G T A B
"" 0 0 0 0 0 0 0 
G  0 
X  0
T  0
X  0
A  0
Y  0         x = max(dp[i - 1][j], dp[i][j - 1]), when A[i - 1] != B[j - 1]
B  0           x = dp[i - 1][j - 1] + 1, when A[i - 1] == B[j - 1]
"""
def LCS(A, B):
    if not A or not B:
        return 0
        
    m, n = len(A), len(B)
    dp = [[0] * (n + 1) for i in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n +  1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


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


# 516. Longest Palindromic - Subsequence - dp O(n^2)
def longestPalindromeSubseq(s):
    if not s:
        return 0

    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
         
    return dp[0][n - 1]
  
