  
# 973. K Closest Points to Origin - heap O(nlogk) 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        origin = [0, 0]
        
        heap = []
        for point in points:
            distance = self.getDistance(point, origin)
            heapq.heappush(heap, (-distance, point[0], point[1]))   # function as max heap 

            if len(heap) > K:
                heapq.heappop(heap)

        output = []
        while len(heap) > 0:
            _, x, y = heapq.heappop(heap)
            output.append([x, y])

        output.reverse()
        return output
    
    
    def getDistance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 
      