
# 4. Median (Kth) of Two Sorted Arrays - merge O(m + n)
#                                      - binary search O(log(m+n))    

class Solution:
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        p1, p2 = 0, 0
        l, r = -1, -1 

        for i in range((m + n) // 2 + 1):
            l = r
            if self.isFirstSmaller(A, p1, B, p2):
                r = A[p1]
                p1 += 1
            else:
                r = B[p2]
                p2 += 1
                
        if (m + n) % 2 == 1:
            return r
        return (l + r) / 2

      
    def isFirstSmaller(self, A, p1, B, p2):
        if p1 >= len(A):
            return False
        if p2 >= len(B):
            return True

        return A[p1] < B[p2]
