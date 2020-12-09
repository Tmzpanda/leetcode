"""
53. Maximum Subarray - greedy O(n)
560. Subarray with Sum Equals - K - hashmap O(n)
974.                          - nK - hashmap O(n)
325. Longest Subarray with Sum Equals K - hashmap O(n)
209. Shortest Subarray with Sum at Least K - positive - sliding window O(n)
862.                                       - negative - mono-queue O(n)
     Longest Subarray with Sum at Most K
1438. Longest Subarray With Absolute Diff at most K - sliding window O(n)
3. Longest Substring Without Repeating Characters - sliding window O(n)

76. Minimum Window with - Target Characters - sliding window O(n)
727.                    - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)

674. Longest Increasing Subarray - greedy O(n)
300. Longest Increasing Subsequence - dp O(n)

"""

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
# 974.                          - nK - hashmap O(n)

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
# 862.                                       - negative - mono-queue O(n)
# Longest Subarray with Sum at Most K
def shortestSubarray(A, K):   
    shortest = sys.maxsize
    psum = 0
    queue = deque([(-1, 0)])   # (end, psum)

    for end in range(len(A)):
        psum += A[end]

        while queue and psum <= queue[-1][1]:
            queue.pop()

        while queue and psum - queue[0][1] >= K:
            shortest = min(shortest, end - queue.popleft()[0])
            
        queue.append((end, psum))

    return shortest if shortest != sys.maxsize else -1


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
# 727.                    - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)

# target chars
class Solution:
    def minWindow(self, s, t):
        targetCharToFreq = self.buildCharToFreq(t)
        sourceCharToFreq = {}
        matched, n = 0, len(targetCharToFreq)
        
        window = ""
        minLen = sys.maxsize
        l, r = 0, 0
        for r in range(len(s)):
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
        return window
        
    def buildCharToFreq(self, s):
        targetCharToFreq = {}
        for c in s:
            targetCharToFreq[c] = targetCharToFreq.get(c, 0) + 1
        return targetCharToFreq


# target sequence
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
  
