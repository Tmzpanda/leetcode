# 875. Minimum Speed to Finish Eating Bananas within H Hours - timeToFinish?H
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        l = 1
        r = max(piles)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.timeToFinish(piles, mid) > H:
                l = mid
            else:
                r = mid
        
        if self.timeToFinish(piles, l) <= H:  # corner case
            return l
        
        return r
    
    
    def timeToFinish(self, piles, speed):
        time = 0
        for p in piles:
            time += math.ceil(p/speed)
            
        return time