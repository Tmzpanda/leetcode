# 862. Shortest Subarray with Sum at Least K 
from collections import deque
def shortestSubarray(nums: List[int], k: int) -> int:
    n = len(nums)
    window_sum = 0
    shortest = sys.maxsize

    queue = deque([(0, 0)])  # (i, window_sum)
    for i in range(n):
        window_sum += nums[i]
        while queue and window_sum - queue[0][1] >= k:
            shortest = min(shortest, i-queue.popleft()[0]+1)
        while queue and window_sum <= queue[-1][1]:    # if negative
            queue.pop()
        queue.append((i+1, window_sum))

    return shortest if shortest != sys.maxsize else -1
