# 658. Find K Closest Elements - binary search merge O(logn + k)    
class Solution:
    def kClosestNumbers(self, A, target, k):
        r = self.findUpperClosest(A, target)
        l = r - 1
    
        res = []
        for _ in range(k):
            if self.isLeftCloser(A, target, l, r):
                res.append(A[l])
                l -= 1
            else:
                res.append(A[r])
                r += 1
                
        return res
    
    def findUpperClosest(self, A, target):
        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                r = mid
            else:
                l = mid
                
        return r
        
    def isLeftCloser(self, A, target, l, r):
        if l < 0:
            return False
        if r >= len(A):
            return True
          
        return target - A[l] <= A[r] - target
