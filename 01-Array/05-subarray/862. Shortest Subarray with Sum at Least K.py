# 862. Shortest Subarray with Sum at Least K - negative exists - mono-queue O(n)
import sys
from collections import deque
def shortestSubarray(A, K):
    shortest = sys.maxsize
    psum = 0
    queue = deque([(-1, 0)])        # (end, psum)

    for end in range(len(A)):
        psum += A[end]

        while queue and psum - queue[0][1] >= K:
            shortest = min(shortest, end - queue.popleft()[0])
        
        while queue and queue[-1][1] >= psum:     # increasing
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