
#********************************************* Shortest Subarray with Sum at Least K **********************************************************

# 209. Minimum Size Subarray Sum
import sys
def shortestSubarray(A, K):
    window_sum = 0
    shortest = sys.maxsize
    start = 0
    
    for end in range(len(A)):
        window_sum += A[end]
        while window_sum >= K:
            shortest = min(shortest, end - start + 1)
            window_sum -= A[start]
            start += 1
            
    return shortest if shortest != sys.maxsize else -1
    
    
    
    
# 862. Shortest Subarray with Sum at Least K
"""" 
sliding window
    [1, 2, 3]     K = 5
     s 
         e 
 
    [1, -1, 2, 3]     K = 5
         s 
               e 
                    
monoqueue - increasing prefix-sums       
            [1, -1, 2, 3]     K = 5
                 ^
psum =  [0,  1,  0, 2, 5]
             ^
           p = [ 0, 2, 5] -> A = [2, 3]
                 ^     ^

sum(A[i] to A[j]) = psum[j + 1] - psum[i]

expand and shrink sliding window
        
""""        
        
import sys
from collections import deque

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
        
        
        
        
        
# Longest Subarray with Sum at Most K - All Positive
def longestSubarray(A, K):
    longest = -sys.maxsize
    window_sum = 0
    start, end = 0, 0
    
    for start in range(len(A)):
        
        while start <= end < len(A) and window_sum <= K:
            longest = max(longest, end - start + 1)
            window_sum += A[end]
            end += 1
            
        window_sum -= A[start]
            
    return longest if longest != -sys.maxsize else -1    
    
    
    
    
    

