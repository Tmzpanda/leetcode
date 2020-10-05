# k closest in a sorted array
# k closest in a BST


class Solution:
    def kClosestNumbers(self, A, target, k):
        right = self.findUpperClosest(A, target)
        left = right - 1
    
        results = []
        for _ in range(k):
            if self.isLeftCloser(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1
        return results
    
    def findUpperClosest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        return end
        
    def isLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
