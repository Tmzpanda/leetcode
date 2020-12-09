"""
53. Maximum Subarray - greedy O(n)
560. Subarray with Sum Equals - K - hashmap O(n)
974.                          - nK - hashmap O(n)
325. Longest Subarray with Sum Equals K - hashmap O(n)
209. Shortest Subarray with Sum at Least K - positive - sliding window O(n)
862. - Shortest Subarray with Sum at Least K - mono-queue O(n)
     - Longest Subarray with Sum at Most K
1438. Longest Subarray With Absolute Diff at most K - sliding window O(n)
3. Longest Substring Without Repeating Characters - sliding window O(n)
76. Minimum Window with - Target Characters - sliding window O(n)
727.                    - Target Subsequence - two pointers O(ST) = O((# of pattern found)*S*T)
674. Longest Increasing Subarray - greedy O(n)
300. Longest Increasing Subsequence - dp O(n)

"""

# Maximum Subarray - greedy O(n) 
def maxSubArray(nums):
    minSum, maxSum = 0, -sys.maxsize
    prefixSum = 0
    
    for num in nums:
        prefixSum += num
        maxSum = max(maxSum, prefixSum - minSum)
        minSum = min(minSum, prefixSum)
        
    return maxSum
