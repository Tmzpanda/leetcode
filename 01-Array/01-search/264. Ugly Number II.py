# 264. Ugly Number II

# heap O(nlogn)
from heapq import heappush, heappop
def nthUglyNumber(n: int) -> int:
  
    heap = []
    heappush(heap, 1)
    seen = set([1])
    factors = [2, 3, 5]
    
    for _ in range(n):
        curr = heappop(heap)
        for factor in factors:
            nxt = curr * factor
            if nxt not in seen:
                seen.add(nxt)
                heappush(heap, nxt)

    return curr
  
  
# 3 pointers O(n)
def nthUglyNumber(n: int) -> int:
    nums = [0] * n
    nums[0] = 1
    
    p1, p2, p3 = 0, 0, 0
    for i in range(1, n):
        nums[i] = min(2 * nums[p1], 3 * nums[p2], 5 * nums[p3])
        if nums[i] == 2 * nums[p1]:
            p1 += 1
        if nums[i] == 3 * nums[p2]:
            p2 += 1
        if nums[i] == 5 * nums[p3]:
            p3 += 1

    return nums[n - 1]

  
  
