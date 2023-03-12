# 215. Kth Largest Element in an Array
# quick select O(n)
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int):      # k -> n-k+1 -> n-k
        n = len(nums)
        return self.quickSelect(nums, 0, n - 1, n - k)
        
    
    def quickSelect(self, nums, start, end, k):
        if start == end:            
            return nums[k]
        
        l, r = start, end
        pivot = random.randint(l, r)
        # partition
        while l <= r:
            while l <= r and nums[l] < nums[pivot]:
                l += 1
            while l <= r and nums[r] > nums[pivot]:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        if k <= r:
            return self.quickSelect(nums, start, r, k)
        if k >= l:
            return self.quickSelect(nums, l, end, k)

        return nums[k]




