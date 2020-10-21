"""
# min heap
# Top K Largest Number


# max heap 
# K Closest Points


# Median in Data Stream

"""

#********************************* min heap **********************************************
# Top K Largest Number - O(nlogk)

from heapq import heappush, heappop
def topk(self, nums, k):   
    if not nums:
        return

    ans = []
    for num in nums:
        heappush(ans, num)

        if len(ans) > k:
            heappop(ans)

    ans.sort(reverse=True)
    return ans
    
    
    
    
#********************************* max heap **********************************************
# K Closest Points - O(nlogk)
import heapq
def kClosest(self, points, origin, k):
    heap = []
    for point in points:
        distance = self.getDistance(point, origin)
        heapq.heappush(heap, (-distance, -point.x, -point.y)) # function as max heap 
        
        if len(heap) > k:
            heapq.heappop(heap)

    output = []
    while len(heap) > 0:
        _, x, y = heapq.heappop(heap)
        output.append([-x, -y])

    output.reverse()
    return output

def getDistance(self, a, b):
    return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
    
    
    
    
