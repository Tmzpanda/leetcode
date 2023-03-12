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